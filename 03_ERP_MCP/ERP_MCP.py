# %%
import numpy as np
import scipy.stats
import statsmodels.stats.multitest
import matplotlib.pyplot as plt
import scipy.ndimage
import pandas as pd

# %%
# Load the group ERP data from the npz file
group_ERP_data = np.load("data/groupERP.npz")
print(group_ERP_data.files)

# %%
# extract relevant data from group_ERP_data
groupERP = group_ERP_data['groupERP']
conditions = list(group_ERP_data['conditions'])
times_in_ms = group_ERP_data['times_in_ms']
ch_names = list(group_ERP_data['ch_names'])
n_subjects = groupERP.shape[3]

print("data shapes:")
print(f"groupERP: {groupERP.shape} (electrodes x timepoints x conditions x subjects), {type(groupERP)}, {groupERP.dtype}")
print(f"conditions: {len(conditions)} (conditions), {type(conditions)}, {conditions}")
print(f"times_in_ms: {times_in_ms.shape} (timepoints), {type(times_in_ms)} {times_in_ms.dtype}")
print(f"ch_names: {len(ch_names)} (electrodes), {type(ch_names)} {ch_names}")

# %% Some data visualization:
condition_color = {
    "familiar": "blue",
    "unfamiliar": "red",
    "scrambled": "green",
}

# generate random colors for each electrode
rng = np.random.RandomState(42)
ch_color = {ch_name:rng.rand(3,) for ch_name in ch_names}

# Plot the data from one electrode, multiple participants, multiple conditions:
Oz_data = groupERP[list(ch_names).index("Oz"), :, :, :]
print(f"shape(one_elec_data)={Oz_data.shape} (timepoints x conditions x subjects)")

def plot_one_elec_conds(one_elec_data, times_in_ms, conditions, condition_color):
    """ Plot all conditions and all participants for a single electrode
        args:
        one_elec_data (timepoints x conditions x subjects)
    """
    grand_average = one_elec_data.mean(axis=2) # (timepoints x conditions)
    grand_average_se = one_elec_data.std(axis=2) / np.sqrt(n_subjects) # (timepoints x conditions)

    plt.figure()
    for cond_idx, condition in enumerate(conditions):
        plt.plot(times_in_ms,
            grand_average[:,cond_idx],
            color=condition_color[condition],
            alpha=1.0,
            label=condition)
        plt.fill_between(x = times_in_ms,
            y1 = grand_average[:,cond_idx]-grand_average_se[:,cond_idx],
            y2 = grand_average[:,cond_idx]+grand_average_se[:,cond_idx],
            color=condition_color[condition],
            alpha=0.3,)
    plt.xlabel("Time (ms)")
    plt.ylabel("Amplitude (uV)")
    plt.legend()

plot_one_elec_conds(Oz_data, times_in_ms, conditions, condition_color)
plt.title('Oz (occipital, midline)')
plt.show()

# Note: this plot generates an underestimate of the differences, because the error patches
# are calculated within each condition (i.e., it doesn't capitalize on the within subject design)

# %% Some more electrodes
plot_one_elec_conds(groupERP[list(ch_names).index("T9"), :, :, :],
                    times_in_ms, conditions, condition_color)
plt.title('T9 (above left ear)')
plt.show()

plot_one_elec_conds(groupERP[list(ch_names).index("T10"), :, :, :],
                    times_in_ms, conditions, condition_color)
plt.title('T10 (above right ear)')
plt.show()

# %%

def compare_conditions(groupERP, conditions, condition1, condition2):
    # calculate the difference wave between the two conditions for each subject,
    # timepoint, and electrode and conduct an uncorrected one-sample t-test on the difference waves.
    # args:
    #   groupERP: group ERP data (electrodes x timepoints x conditions x subjects)
    #   conditions: condition labels (conditions)
    #   condition1: first condition to compare (condition)
    #   condition2: second condition to compare (condition)
    # returns:
    #   difference_wave: difference wave (electrodes x timepoints x subjects)
    #   t_stat_map: t-statistic map (electrodes x timepoints)
    #   p_values: p-values (electrodes x timepoints)

    # extract data for the two conditions
    assert len(conditions) == groupERP.shape[2], f"len(conditions) {len(conditions)} does not match groupERP.shape[2] {groupERP.shape[2]}"
    assert condition1 in conditions, f"condition1 {condition1} not found in conditions"
    assert condition2 in conditions, f"condition2 {condition2} not found in conditions"
    condition1_data = groupERP[:, :, conditions.index(condition1), :] # (subjects x timepoints)
    condition2_data = groupERP[:, :, conditions.index(condition2), :] # (subjects x timepoints)

    difference_wave = condition1_data -  condition2_data

    # calculate t-statistic map
    t_test_results = scipy.stats.ttest_1samp(
        difference_wave,
        axis=-1, # we want to average over subjects
        popmean=0 # we want to test the difference wave against 0
    )

    t_stat_map = t_test_results.statistic
    p_values = t_test_results.pvalue

    return difference_wave, t_stat_map, p_values

# %% Compare unfamiliar and scrambled faces
difference_wave, t_stat_map, uncorrected_p_values = compare_conditions(groupERP, conditions, "unfamiliar","scrambled")
grand_avg_diff = difference_wave.mean(axis=-1) # average over subjects

# let's inspect the shapes of the results:
print("difference_wave.shape:", difference_wave.shape)
print("grand_avg_diff.shape:", grand_avg_diff.shape)
print("t_stat_map.shape:", t_stat_map.shape)
print("uncorrected_p_values.shape:", uncorrected_p_values.shape)

# %% Plot the difference wave as a butterfly plot
def plot_difference_wave(wave, times_in_ms, is_significant=None):
    """ Plot the difference wave as a butterfly plot
        args:
        wave (electrodes x timepoints )
        times_in_ms (timepoints)
        is_significant (electrodes x timepoints): if not None, plot a red dot at each timepoint that is significant
    """

    plt.figure()
    n_electrodes = wave.shape[0]
    for i_electrode in range(n_electrodes):
        plt.plot(times_in_ms, wave[i_electrode], color='k', alpha=0.2)
        if is_significant is not None:
            significant_timepoints = np.where(is_significant[i_electrode])[0]
            plt.plot(times_in_ms[significant_timepoints],
                     wave[i_electrode, significant_timepoints], 'ro')
    plt.xlabel("Time (ms)")

plot_difference_wave(grand_avg_diff,
    times_in_ms,
    is_significant=uncorrected_p_values < 0.05)
plt.title("Difference wave between unfamiliar and scrambled faces (uncorrected p < 0.05)")
plt.ylabel("Amplitude (uV)")
plt.show()

# %% Plot the t-statistic butterfly plot

plot_difference_wave(t_stat_map,
    times_in_ms,
    is_significant=uncorrected_p_values < 0.05)
plt.title("T-value between unfamiliar and scrambled faces (uncorrected p < 0.05)")
plt.ylabel("T")
plt.show()


# %% Holm-Bonferroni correction
HB_is_significant, pvals_HB_corrected, _, _ = statsmodels.stats.multitest.multipletests(
    uncorrected_p_values.flatten(),
    method='holm',
    alpha=0.05,
    is_sorted=False,
    returnsorted=False
)
# Since we flattened the p-values, we need to reshape them back to the original shape
pvals_HB_corrected = pvals_HB_corrected.reshape(uncorrected_p_values.shape)
HB_is_significant = HB_is_significant.reshape(uncorrected_p_values.shape)

plot_difference_wave(grand_avg_diff, # average over subjects
    times_in_ms,
    is_significant=HB_is_significant)
plt.title("Difference wave between unfamiliar and scrambled faces (Holm-Bonferroni corrected p < 0.05)")
plt.show()

plot_difference_wave(t_stat_map,
    times_in_ms,
    is_significant=HB_is_significant)
plt.title("T-value between unfamiliar and scrambled faces (Holm-Bonferroni corrected p < 0.05)")
plt.show()

# %% Cluster-based permutation test

def detect_clusters(t_stat_map, t_threshold, scoring_method="length"):
    # detects clusters of significant points within each electrode using
    # a labeling algorithm from scipy.ndimage.measurements.
    # This is a relative simple clustering approach
    # because we are only clustering within each electrode.
    # A stronger approach would be to cluster across timepoints AND neighboring electrodes.
    #
    # args:
    #   t_stat_map (electrodes x timepoints): t-statistic map
    #   t_threshold (float): threshold for t-statistic
    #   scoring_method (str): "length" or "sum" (how to score clusters)
    # returns:
    #   clusters (list): list of of dictionaries, one for each electrode, with keys:
    #    "electrode" (int): electrode index
    #    "start_timepoint" (int): start timepoint of cluster
    #    "end_timepoint" (int): end timepoint of cluster
    #    "score" (int): score of cluster (length or sum of t-statistic values)
    #    "sign" (int): sign of cluster (1 or -1)

    clusters = []
    n_electrodes = t_stat_map.shape[0]
    for i_electrode in range(n_electrodes):
        for sign in [-1, 1]:
            if sign == 1:
                above_threshold = t_stat_map[i_electrode] > t_threshold
            elif sign == -1:
                above_threshold = t_stat_map[i_electrode] < -t_threshold

            if np.any(above_threshold):
                # Use scipy.ndimage.label to detect clusters
                label, n_clusters = scipy.ndimage.label(above_threshold)
                # label is an array of the same shape as above_threshold
                # where each cluster is assigned a unique integer value
                # and all non-cluster points are assigned 0
                # n_clusters is the number of clusters found

                # Loop over clusters and add them to the list
                for cluster_idx in range(1, n_clusters + 1):
                    t0 = np.where(label == cluster_idx)[0][0] # first timepoint of cluster
                    t1 = np.where(label == cluster_idx)[0][-1] # last timepoint of cluster
                    cluster = {}
                    cluster["electrode"] = i_electrode
                    cluster["start_timepoint"] = t0
                    cluster["end_timepoint"] = t1
                    if scoring_method == "length":
                        cluster["score"] = t1 - t0 + 1
                    elif scoring_method == "sum":
                        cluster["score"] = np.abs(
                            np.sum(
                                t_stat_map[i_electrode, t0:t1+1]
                            )
                        )
                    else:
                        raise ValueError("scoring_method must be 'length' or 'sum'")
                    cluster["sign"] = sign
                    clusters.append(cluster)
    return clusters

# let's try it out
# pandas: print the full dataframe
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# %% length-based score (cluster length)
observed_clusters = detect_clusters(t_stat_map, t_threshold=5, scoring_method="length")
cluster_table = pd.DataFrame(observed_clusters) # form a nice table of clusters
print(cluster_table)

# %% sum-based score (cluster mass)
observed_clusters = detect_clusters(t_stat_map, t_threshold=5, scoring_method="sum")
cluster_table = pd.DataFrame(observed_clusters) # form a nice table of clusters
print(cluster_table)


# %%
def cluster_permutation_test(difference_wave, n_permutations, t_threshold, scoring_method="length", return_null_distribution=False):

    """ Cluster-based permutation FWER-controlled test for ERP differences
        between two conditions.

        Args:
            difference_wave (electrodes x timepoints x subjects): difference wave between two conditions
            n_permutations (int): number of permutations to perform
            t_threshold (float): threshold for t-statistic
            scoring_method (str): "length" or "sum" (how to score clusters)
        Returns:
            p_value (float): p-value of the test
            observed_clusters (list): list of of dictionaries, one for each electrode, with keys:
                "electrode" (int): electrode index
                "start_timepoint" (int): start timepoint of cluster
                "end_timepoint" (int): end timepoint of cluster
                "score" (int): score of cluster (length or sum of t-statistic values)
                "sign" (int): sign of cluster (1 or -1)
                "counter" (int): counter of how many permutations have a cluster with a score as high as the observed cluster
                "p_value" (float): FWER-corrected p-value of cluster
    """

    n_subjects = difference_wave.shape[-1]

    t_test_results = scipy.stats.ttest_1samp(
            difference_wave,
            axis=-1, # we want to average over subjects
            popmean=0, # we want to test the difference wave against 0
        )

    observed_t_stat_map = t_test_results.statistic
    observed_clusters = detect_clusters(observed_t_stat_map, t_threshold, scoring_method)

    # We will add a counter to each cluster to keep track of how many permutations
    # have a cluster with a score as high as the observed cluster

    for cluster in observed_clusters:
        cluster["counter"] = 0

    if return_null_distribution:
        null_distribution = []

    for i_permutation in range(n_permutations):

        # permute the difference wave
        # generate a random permutation of 1s and -1s

        subject_random_sign = np.random.choice([-1, 1], size=n_subjects)
        # important: we apply the same random sign to all electrodes and all timepoints
        # of the difference wave within a subject.

        permuted_diff_wave = difference_wave * np.expand_dims(subject_random_sign, axis=(0, 1))
        # permuted_diff_wave is 1 x 1 x subjects, to match the shape of difference_wave (electrodes x timepoints x subjects)

        # # The following line is wrong, it permutes the sign of each timepoint and electrode separately
        # permuted_diff_wave = difference_wave * np.random.choice([-1, 1], size=difference_wave.shape)

        permuted_t_stat_map = scipy.stats.ttest_1samp(
            permuted_diff_wave,
            axis=-1, # we want to average over subjects
            popmean=0 # we want to test the difference wave against 0
        ).statistic

        clusters_under_H0 = detect_clusters(permuted_t_stat_map, t_threshold, scoring_method)

        # obtain a single (scalar) maximum score for this permutation
        if len(clusters_under_H0) > 0:
            max_score = np.max(
                [cluster["score"] for cluster in clusters_under_H0]
                )
        else:
            max_score = 0

        if return_null_distribution:
            null_distribution.append(max_score)

        for observed_cluster in observed_clusters:
            if observed_cluster["score"] <= max_score:
                observed_cluster["counter"] += 1
        # note: this is a simple version, where we use scores that can only be positive

    # calculate FWER-corrected p-values for each observed cluster
    for cluster in observed_clusters:
        cluster["p_value"] = (cluster["counter"]+1) / (n_permutations + 1)
    if return_null_distribution:
        return observed_clusters, null_distribution
    else:
        return observed_clusters

def clusters_to_significant_time_windows(observed_clusters, n_electrodes, n_timepoints, alpha=0.05):
    """ convert a cluster list to a numpy array of significant timepoints
        args:
            observed_clusters (list)
            n_electrodes (int)
            n_timepoints (int)
            alpha (float)
        returns:
            significant_timepoints (numpy array), shape: (n_electrodes, n_timepoints)
    """
    significant_timepoints = np.zeros((n_electrodes, n_timepoints))
    for cluster in observed_clusters:
        significant_timepoints[cluster["electrode"], cluster["start_timepoint"]:cluster["end_timepoint"]] = cluster["p_value"] < alpha
    return significant_timepoints

observed_clusters, null_distribution = cluster_permutation_test(
    difference_wave,
    n_permutations=1000,
    t_threshold=5.0,
    scoring_method="sum",
    return_null_distribution=True)

plt.figure()
plt.hist(null_distribution, bins=50)
plt.xlabel("cluster score")
plt.ylabel("count")
plt.show()

# let's drop the non-significant clusters
observed_clusters = [cluster for cluster in observed_clusters if cluster["p_value"] < 0.05]
cluster_table = pd.DataFrame(observed_clusters) # form a nice table of clusters
print(cluster_table)

cluster_corrected_significant_timepoints = clusters_to_significant_time_windows(observed_clusters, n_electrodes=difference_wave.shape[0], n_timepoints=difference_wave.shape[1], alpha=0.05)
plot_difference_wave(t_stat_map, times_in_ms, is_significant=cluster_corrected_significant_timepoints)
plt.ylabel("T")
plt.title("cluster-corrected significant timepoints (cluster forming threshold t=4, cluster p<0.05)")
plt.show()


# It might be interesting to repeat the code above with a different cluster forming threshold (e.g. 3 instead of 5).

# %%
