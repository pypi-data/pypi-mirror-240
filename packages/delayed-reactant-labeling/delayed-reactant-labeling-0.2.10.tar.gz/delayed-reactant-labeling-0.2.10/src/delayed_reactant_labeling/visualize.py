from __future__ import annotations

import os
from typing import Optional
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tqdm import tqdm
from delayed_reactant_labeling.predict import InvalidPredictionError
from delayed_reactant_labeling.optimize import RateConstantOptimizerTemplate, OptimizerProgress


class VisualizeSingleSolution:
    def __init__(self,
                 path: str,
                 description: str,
                 rate_constant_optimizer: RateConstantOptimizerTemplate,
                 index_constant_values: Optional[np.ndarray] = None,
                 isomers: Optional[list[str]] = None,
                 dpi: int = 600,
                 ):
        self.path = path
        self.description = description
        self._best_prediction = None
        self.rate_constant_optimizer = rate_constant_optimizer
        self.progress = self.rate_constant_optimizer.load_optimization_progress(path)
        self.isomers = isomers
        self.index_constant_values = index_constant_values
        self.dpi = dpi

    @property
    def best_prediction(self) -> pd.DataFrame:
        if self._best_prediction is None:
            # recompute the best prediction so that we can make plots of it.
            # self.experimental, self._prediction = self.create_prediction(_rate_constants=self.progress.best_rates)
            self._best_prediction = self.rate_constant_optimizer.create_prediction(
                x=self.progress.best_X.to_numpy(), x_description=self.progress.x_description)
        return self._best_prediction

    def show_error_over_time(self, compound_ratio: Optional[list[str]] = None, compound_ratio_points: int = 100) -> \
            tuple[plt.Figure, plt.Axes]:
        """Shows the enantiomeric ratio if compound_ratio is given, and MAE, as a function of the iteration number.
        The compound ratio must be redetermined for each point in the compound_ratio_points"""
        # explore the solution
        fig, ax = plt.subplots()
        ax.scatter(range(1, 1 + len(self.progress.all_errors)), self.progress.all_errors, alpha=0.3)

        if compound_ratio is not None:
            ax2 = ax.twinx()
            found_ratio = []
            ratio_sampled = np.linspace(0, len(self.progress.all_X) - 1, compound_ratio_points).round(0).astype(int)
            for iteration in ratio_sampled:
                pred = self.rate_constant_optimizer.create_prediction(
                    x=self.progress.all_X.iloc[iteration, :],
                    x_description=self.progress.all_X.columns)
                found_ratio.append((pred[compound_ratio[0]] / pred[compound_ratio[1]].sum(axis=1))[-100:].mean())

            ax2.scatter(ratio_sampled, found_ratio, alpha=0.3, color="C1")
            ax2.set_ylabel("ratio", color="C1")

        ax.set_xlabel("iteration")
        ax.set_ylabel("sum of MAE", color="C0")
        ax.set_title(f"{self.description}")
        fig.savefig(f"{self.path}error_over_time.png", dpi=self.dpi)
        fig.savefig(f"{self.path}error_over_time.svg", dpi=self.dpi)
        return fig, ax

    def show_comparison_with_literature(self,
                                        desired_k: list[str],
                                        literature_k: pd.Series) -> tuple[plt.Figure, plt.Axes]:
        """
        Show a comparison between the found rates and some given rates. Rate name should be {k}_{isomer}.
        :param desired_k: The rate constants that should be shown.
        :param literature_k: Series containing the constants from literature.
        :return: Figure, Axes
        """
        fig, axs = plt.subplots(3, figsize=(8, 8))
        for ax, isomer in zip(axs, self.isomers):
            ax.set_title(f"{isomer}")

            rate_found = []
            rate_lit = []

            for k in desired_k:
                # if a key is not found, it will be replaced by nan, which will not show up in the plot
                rate_found.append(self.progress.best_X.get(f"{k}_{isomer}", np.nan))
                rate_lit.append(literature_k.get(f"{k}_{isomer}", np.nan))

            x = np.arange(len(rate_found))
            multiplier = -0.5
            width = 0.4
            max_val = max([max(rate_found), max(rate_lit)])
            settings = {"ha": "center", "fontweight": "bold"}
            for vals, descr in zip([rate_found, rate_lit], ["found", "lit."]):
                ax.bar(x + width * multiplier,
                       vals,
                       width,
                       label=descr)
                for val, val_x in zip(vals, x + width * multiplier):
                    if val > 0.005:
                        form = f"{val:.3f}"
                    else:
                        form = f"{val:.0e}"

                    if val < 0.5 * max_val:
                        ax.text(val_x, val + 0.02 * max_val, form, color="k", **settings)
                    else:
                        ax.text(val_x, val - 0.09 * max_val, form, color="w", **settings)
                multiplier += 1

            ax.set_xticks(x, desired_k, rotation=90, fontsize="small")
        axs[-1].legend()
        fig.suptitle(f"{self.description}")
        fig.supylabel("rate constant intensity")
        fig.tight_layout()
        fig.savefig(f"{self.path}comparison_with_literature.png", dpi=self.dpi)
        fig.savefig(f"{self.path}comparison_with_literature.svg", dpi=self.dpi)
        return fig, axs

    def show_optimization_path_in_pca(self, create_3d_video: bool = False, fps: int = 30) -> tuple[
            plt.Figure, list[plt.Axes]]:
        from sklearn.decomposition import PCA

        # explore pca space
        fig = plt.figure(figsize=(8, 8))
        gs = fig.add_gridspec(2, 2, width_ratios=(1, 4), height_ratios=(4, 1),
                              left=0.15, right=0.83, bottom=0.15, top=0.83,
                              wspace=0.05, hspace=0.05)
        ax = fig.add_subplot(gs[0, 1])

        pca = PCA().fit(X=self.progress.all_X)
        scattered = ax.scatter(self.progress.all_X.dot(pca.components_[0]),
                               self.progress.all_X.dot(pca.components_[1]),
                               c=np.arange(len(self.progress.all_X)))
        ax.tick_params(top=True, right=True, labeltop=True, labelright=True)
        ax_bbox = ax.get_position(original=True)
        cax = plt.axes([0.85, ax_bbox.ymin, 0.05, ax_bbox.size[1]])
        cbar = plt.colorbar(scattered, cax=cax)
        cbar.set_label("iteration")

        ax_pc0 = fig.add_subplot(gs[1, 1])
        ax_pc1 = fig.add_subplot(gs[0, 0])

        x = np.arange(sum(~self.index_constant_values))
        xticks = self.progress.x_description[~self.index_constant_values]

        ax_pc0.bar(x, pca.components_[0][~self.index_constant_values])
        ax_pc1.barh(x, pca.components_[1][~self.index_constant_values])

        ax_pc0.set_xlabel(f"component 0, explained variance {pca.explained_variance_ratio_[0]:.2f}")
        ax_pc0.set_xticks(x, xticks, rotation=90, fontsize="small")

        ax_pc1.set_ylabel(f"component 1, explained variance {pca.explained_variance_ratio_[1]:.2f}")
        ax_pc1.set_yticks(x, xticks, fontsize="small")

        def create_3d_video_animation():
            fig3d = plt.figure()
            ax3d = fig3d.add_subplot(projection="3d")

            ax3d.scatter(self.progress.all_X.dot(pca.components_[0]),
                         self.progress.all_X.dot(pca.components_[1]),
                         self.progress.all_X.dot(pca.components_[2]),
                         c=np.arange(len(self.progress.all_X)))
            ax3d.tick_params(bottom=False, left=False,
                             labelbottom=False, labelleft=False)

            # Rotate the axes and update
            files = []
            files_folder = f"{self.path}/pca_rotation_animation"
            os.makedirs(files_folder)

            for n, angle in tqdm(enumerate(range(0, 360 * 4 + 1))):
                # Normalize the angle to the range [-180, 180] for display
                angle_norm = (angle + 180) % 360 - 180

                # Cycle through a full rotation of elevation, then azimuth, roll, and all
                elev = azim = roll = 0
                if angle <= 360:
                    elev = angle_norm
                elif angle <= 360 * 2:
                    azim = angle_norm
                elif angle <= 360 * 3:
                    roll = angle_norm
                else:
                    elev = azim = roll = angle_norm

                # Update the axis view and title
                ax3d.view_init(elev, azim, roll)
                ax3d.set_title('Elevation: %d°, Azimuth: %d°, Roll: %d°' % (elev, azim, roll))
                file = f"{files_folder}/{n}.jpg"
                files.append(file)
                fig3d.savefig(file)

            import moviepy.video.io.ImageSequenceClip
            clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(files, fps=fps)
            clip.write_videofile(f'{self.path}pca_rotation.mp4')

        if create_3d_video:
            create_3d_video_animation()

        fig.suptitle(f"{self.description}")
        fig.savefig(f"{self.path}path_in_pca_space.png", dpi=self.dpi)
        fig.savefig(f"{self.path}path_in_pca_space.svg", dpi=self.dpi)
        return fig, [ax, ax_pc0, ax_pc1]

    def show_error_contributions(self) -> tuple[plt.Figure, plt.Axes]:
        errors = self.rate_constant_optimizer.calculate_errors(self.best_prediction)
        weighed_errors = self.rate_constant_optimizer.weigh_errors(errors)
        fig, ax = plt.subplots()
        weighed_errors.plot.bar(ax=ax)
        ax.set_ylabel("MAE")
        ax.set_xlabel("rate constant")
        fig.tight_layout()
        fig.savefig(f"{self.path}bar_plot_of_all_errors.png", dpi=self.dpi)
        fig.savefig(f"{self.path}bar_plot_of_all_errors.svg", dpi=self.dpi)
        return fig, ax

    def show_enantiomer_ratio(self, intermediates: list[str], experimental: pd.DataFrame) -> tuple[plt.Figure, plt.Axes]:
        fig, ax = plt.subplots()
        ax.set_title(self.description)
        plotted_label = False
        for x, intermediate in enumerate(intermediates):
            total_pred = self.best_prediction[[f"{intermediate}{isomer}" for isomer in self.isomers]].sum(axis=1)
            for i, isomer in enumerate(self.isomers):
                if not plotted_label:
                    label = f"predicted {isomer}"
                else:
                    label = None
                y_pred = self.best_prediction[f"{intermediate}{isomer}"] / total_pred
                y_pred = y_pred[-60:].mean()
                ax.scatter(x, y_pred, label=label, marker="^", alpha=0.7, color=f"C{i}")
                ax.text(x + 0.07, y_pred, f"{y_pred * 100:.1f}%", ha="left", va="center")
            plotted_label = True

        plotted_label = False
        for x, intermediate in enumerate(intermediates):
            try:
                total_exp = experimental[[f"{intermediate}{isomer}" for isomer in self.isomers]].sum(
                    axis=1)
                for i, isomer in enumerate(self.isomers):
                    if not plotted_label:
                        label = f"experimental {isomer}"
                    else:
                        label = None
                    y_exp = experimental[f"{intermediate}{isomer}"] / total_exp
                    y_exp = y_exp[-60:].mean()
                    ax.scatter(x, y_exp, label=label, marker="x", alpha=0.7, color=f"C{i}")
                plotted_label = True
            except KeyError:
                print(f"could not find {intermediate} in the experimental data. skipping...")

        ax.set_ylabel("isomer fraction")
        ax.legend()
        ax.set_xticks(range(len(intermediates)), intermediates)
        ax.set_xlabel("compound")
        xl, xu = ax.get_xlim()
        ax.set_xlim(xl, xu + 0.2)
        fig.tight_layout()
        fig.savefig(f"{self.path}enantiomer_ratio.png", dpi=self.dpi)
        fig.savefig(f"{self.path}enantiomer_ratio.svg", dpi=self.dpi)
        return fig, ax

    def animate_rate_over_time(
            self,
            n_frames=300,
            fps=30
    ) -> None:
        import moviepy.video.io.ImageSequenceClip

        n_iter = self.progress.n_iterations
        if n_frames > n_iter:
            raise ValueError("specified to analyze more frames than available iterations")

        fig, (ax_rates, ax_error) = plt.subplots(2)

        ticks = self.progress.all_X.columns[~self.index_constant_values]
        x = np.arange(len(ticks))

        ax_error.set_xlim(0, n_iter - 1)
        files = []
        files_folder = f"{self.path}/animation_rate_over_time"
        try:
            os.makedirs(files_folder)
        except FileExistsError:
            print("Already a folder containing the pca_rotation exists. skipping...")
            return None

        for i in tqdm(np.linspace(0, n_iter - 1, n_frames).round().astype(int)):
            # rate plot
            rates = self.progress.all_X.loc[i, :]
            ax_rates.clear()
            ax_rates.bar(x, rates.iloc[self.index_constant_values])

            ax_rates.set_xticks(x, ticks, rotation=90, fontsize="small")
            ax_rates.set_ylabel("k")
            ax_rates.legend(loc=1)
            ax_rates.set_title("found rate")

            # update the error plot
            ax_error.scatter(i, self.progress.all_errors[i], color="tab:blue")

            ax_error.set_xlabel("iteration")
            ax_error.set_ylabel("MAE", color="tab:blue")
            fig.suptitle(f"{self.description}")

            file = f"{files_folder}/frame_{i}.jpg"
            files.append(file)
            fig.tight_layout()
            fig.savefig(file)

        clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(files, fps=fps)
        clip.write_videofile(f"{self.path}visualized_rate_over_time.mp4")

    def show_rate_sensitivity(self,
                              lower_power: int = -6,
                              upper_power: int = 2,
                              steps: int = 101,
                              threshold=3) -> (plt.Figure, plt.Axes):
        from mpl_toolkits.axes_grid1 import make_axes_locatable

        x_value = np.logspace(lower_power, upper_power, steps)

        ticks = self.progress.best_X[~self.index_constant_values]
        errors = np.full((len(x_value), len(ticks)), np.nan)

        # loop over all non-constant values and adjust those
        for col, key in enumerate(tqdm(self.progress.best_X[~self.index_constant_values].keys())):
            for row, adjusted_x in enumerate(x_value):
                # insert all values into the plot
                best_X = self.progress.best_X.copy()
                best_X[key] = adjusted_x
                try:
                    prediction = self.rate_constant_optimizer.create_prediction(
                        x=best_X.to_numpy(), x_description=self.progress.x_description)
                    unweighed_error = self.rate_constant_optimizer.calculate_errors(prediction)
                    found_error = self.rate_constant_optimizer.calculate_total_error(unweighed_error)
                except InvalidPredictionError:
                    found_error = np.nan
                errors[row, col] = found_error

        min_error = np.nanmin(errors)
        errors[errors > threshold * min_error] = threshold * min_error

        fig, ax = plt.subplots()
        im = ax.imshow(errors, origin="lower", aspect="auto")

        ax.set_xticks(np.arange(len(ticks)), ticks.index, fontsize="small")
        ax.tick_params(axis='x', rotation=45)

        n_orders_of_magnitude = int(upper_power - lower_power + 1)
        ind = np.linspace(0, len(x_value) - 1, n_orders_of_magnitude)  # .round(0).astype(int)
        yticks = [f"{y:.0e}" for y in np.logspace(lower_power, upper_power, n_orders_of_magnitude)]
        ax.set_yticks(ind, yticks)
        ax.set_ylabel("adjusted value")

        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", "5%", pad="3%")
        fig.colorbar(im, cax=cax, label="MAE")
        ax.set_title(f"{self.description}")
        fig.tight_layout()
        fig.savefig(f"{self.path}sensitivity_of_rate.png", dpi=self.dpi)
        fig.savefig(f"{self.path}sensitivity_of_rate.svg", dpi=self.dpi)

        return fig, ax


class VisualizeMultipleSolutions:
    def __init__(self, path, max_guess=np.inf):
        """Loads the data in the path. For each """
        guess_files = os.listdir(path)

        self.complete_all_X = []
        self.complete_initial_X = []
        self.complete_optimal_X = []
        self.complete_found_error = []
        self.x_description = None

        for n, guess in tqdm(enumerate(guess_files)):
            if n > max_guess:
                break

            guess_path = f"{path}/{guess}"
            progress = OptimizerProgress(guess_path)

            self.complete_all_X.append(progress.all_X)
            self.complete_initial_X.append(progress.all_X.iloc[0, :])
            self.complete_optimal_X.append(progress.best_X)
            self.complete_found_error.append(progress.best_error)

            if self.x_description is None:
                self.x_description = progress.x_description

        # complete all X is not here as it is already a 2D matrix
        self.complete_initial_X = np.array(self.complete_initial_X)
        self.complete_optimal_X = np.array(self.complete_optimal_X)
        self.complete_found_error = np.array(self.complete_found_error)

    def show_error_all_runs(self, top_n=-1) -> tuple[plt.Figure, plt.Axes]:
        if top_n == -1:
            top_n = len(self.complete_found_error)
        ind = np.argsort(self.complete_found_error)[:top_n]

        fig, ax = plt.subplots(layout='tight')
        ax.scatter(np.arange(top_n), self.complete_found_error[ind])
        ax.set_xlabel('run number (sorted by error)')
        ax.set_ylabel('error')
        return fig, ax

    def show_summary_all_runs(self,
                              rco: RateConstantOptimizerTemplate,
                              compound_ratio: list[str, list[str]],
                              top_n: int = -1,
                              max_error: float = 0.5) -> tuple[plt.Figure, plt.Axes]:
        fig, ax = plt.subplots(layout='tight')
        ind = np.argsort(self.complete_found_error)[:top_n]

        found_ratio = []
        for run_index in ind:
            pred = rco.create_prediction(self.complete_optimal_X[run_index].values, self.complete_optimal_X[run_index].index)
            found_ratio.append(pred[compound_ratio[0]] / pred[compound_ratio[1]].sum(axis=1))  # TODO double check this

        error = np.array(self.complete_found_error)
        error[error > max_error] = max_error
        im = ax.scatter(np.arange(len(ind)),
                        found_ratio[ind],
                        c=np.array(self.complete_found_error)[ind])

        fig.colorbar(im, ax=ax, label='error')
        ax.set_xlabel('run number (sorted by error)')
        ax.set_ylabel('ratio')
        return fig, ax

    def show_rate_constants(self, max_error: float, index_constant_values: np.ndarray = None) -> tuple[plt.Figure, plt.Axes]:
        ind_allowed_error = np.array(self.complete_found_error) < max_error
        df = pd.DataFrame(np.array(self.complete_optimal_X)[ind_allowed_error], columns=self.x_description)
        if index_constant_values is not None:
            df = df.loc[:, ~index_constant_values]

        fig, ax = plt.subplots(layout="tight")
        ax.boxplot(df)
        ax.set_title("distribution of optimal rates")
        _ = ax.set_xticks(1 + np.arange(len(df.columns)), df.columns, rotation=90)
        ax.set_yscale("log")
        ax.set_ylabel("value of k")
        return fig, ax

    def show_biplot(self,
                    max_error: float,
                    pc1: int = 0,
                    pc2: int = 1,
                    ax: plt.Axes = None):
        from sklearn.decomposition import PCA
        from sklearn.preprocessing import StandardScaler

        if ax is None:
            fig, ax = plt.subplots()
        else:
            fig = ax.figure

        data = []
        for error, initial, optimal in zip(self.complete_found_error, self.complete_initial_X, self.complete_optimal_X):
            if error > max_error:
                continue
            data.append(initial)
            data.append(optimal)

        data = pd.DataFrame(data).reset_index(drop=True)  # by converting to df first, we assure that the columns are aligned
        scaler = StandardScaler()
        scaler.fit(X=data.to_numpy())  # scale each rate so its std deviation becomes 1
        pca = PCA().fit(X=scaler.transform(data.to_numpy()))

        # scores
        for error, initial, optimal in zip(self.complete_found_error, self.complete_initial_X, self.complete_optimal_X):
            if error > max_error:
                continue
            ax.scatter(
                x=scaler.transform(initial.to_numpy().reshape(1, -1)).dot(pca.components_[pc1]),
                y=scaler.transform(initial.to_numpy().reshape(1, -1)).dot(pca.components_[pc2]),
                marker='o', color='tab:blue'
            )
            ax.scatter(
                x=scaler.transform(optimal.to_numpy().reshape(1, -1)).dot(pca.components_[pc1]),
                y=scaler.transform(optimal.to_numpy().reshape(1, -1)).dot(pca.components_[pc2]),
                marker='*', color='tab:orange'
            )
        ax.scatter(np.nan, np.nan, color="tab:blue", marker="o", label="initial")
        ax.scatter(np.nan, np.nan, color="tab:orange", marker="*", label="optimal")
        ax.legend()

        # maximize the size of the loadings
        x_factor = abs(np.array(ax.get_xlim())).min() / pca.components_[pc1].max()
        y_factor = abs(np.array(ax.get_ylim())).min() / pca.components_[pc2].max()

        # loadings
        for rate, loading1, loading2 in zip(data.columns, pca.components_[pc1], pca.components_[pc2]):
            ax.plot([0, loading1*x_factor], [0, loading2*y_factor], color='tab:gray')
            ax.text(loading1*x_factor, loading2*y_factor, rate, ha='center', va='bottom')

        ax.set_title('biplot')
        ax.set_xlabel(f'PC {pc1}, explained variance {pca.explained_variance_ratio_[pc1]:.2f}')
        ax.set_ylabel(f'PC {pc2}, explained variance {pca.explained_variance_ratio_[pc2]:.2f}')

        return fig, ax
