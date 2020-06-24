
import shutil
import subprocess

from mtuq.graphics.beachball import plot_beachball, misfit_vs_depth

from mtuq.graphics.uq import plot_misfit, plot_likelihood, plot_marginal
from mtuq.graphics.uq_dc import plot_misfit_dc
from mtuq.graphics.uq_vw import plot_misfit_vw, plot_likelihood_vw, plot_marginal_vw
from mtuq.graphics.uq_force import plot_misfit_force, plot_likelihood_force, plot_marginal_force

from mtuq.graphics.waveform import plot_data_synthetics, plot_data_greens


