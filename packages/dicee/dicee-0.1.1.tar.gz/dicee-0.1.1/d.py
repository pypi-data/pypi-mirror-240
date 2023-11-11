from dicee import KGE
import pandas as pd
from dicee.static_funcs import get_er_vocab
from dicee.eval_static_funcs import evaluate_link_prediction_performance_with_reciprocals
model = KGE(url="https://files.dice-research.org/projects/DiceEmbeddings/KINSHIP-Keci-dim128-epoch256-KvsAll")
result=model.get_eval_report()
print(model.predict(h="person49", r="term12", t="person39"))

train_triples = pd.read_csv("KGs/KINSHIP/train.txt",
                            sep="\s+",
                            header=None, usecols=[0, 1, 2],
                            names=['subject', 'relation', 'object'],
                            dtype=str).values.tolist()
valid_triples = pd.read_csv("KGs/KINSHIP/valid.txt",
                            sep="\s+",
                            header=None, usecols=[0, 1, 2],
                            names=['subject', 'relation', 'object'],
                            dtype=str).values.tolist()
test_triples = pd.read_csv("KGs/KINSHIP/test.txt",
                           sep="\s+",
                           header=None, usecols=[0, 1, 2],
                           names=['subject', 'relation', 'object'],
                           dtype=str).values.tolist()
all_triples = train_triples + valid_triples + test_triples

er_vocab=get_er_vocab(all_triples)
print(result["Train"])
print(evaluate_link_prediction_performance_with_reciprocals(model, triples=train_triples,
                                                               er_vocab=er_vocab))
print(result["Val"])
print(evaluate_link_prediction_performance_with_reciprocals(model, triples=valid_triples,
                                                             er_vocab=er_vocab))
print(result["Test"])
print(evaluate_link_prediction_performance_with_reciprocals(model, triples=test_triples,
                                                              er_vocab=er_vocab))



exit(1)
exit(1)
from dicee import Execute, KGE
from dicee.config import Namespace
import shutil
from dicee.static_funcs import create_recipriocal_triples, get_er_vocab
from dicee.eval_static_funcs import evaluate_link_prediction_performance_with_bpe_reciprocals
import pandas as pd
from combine_knowledge_graph import create_new_kg

"""
args = Namespace()
args.model = "Keci"
args.p = 0
args.q = 1
args.num_epochs = 100
args.lr = 0.001
args.dataset_dir = "KGs/UMLS/"
args.scoring_technique = 'KvsAll'
args.eval_model = 'train_val_test'
args.byte_pair_encoding = True
result = Execute(args).start()
print(result)
"""

exit(1)


def save_embeddings():
    triples = pd.read_csv("KGs/Countries-S3/train.txt",
                          sep="\s+",
                          header=None, usecols=[0, 1, 2],
                          names=['subject', 'relation', 'object'],
                          dtype=str)

    countries = list(set(triples[triples.relation == "locatedin"]["subject"].tolist()))

    base_model = KGE("Experiments/2023-10-31 14-54-28.221507")
    attentive_bpe_model = KGE("Experiments/2023-10-31 14-56-38.631855")

    base_embeddings = base_model.get_entity_embeddings(countries)
    ape_embeddings = attentive_bpe_model.get_entity_embeddings(countries)

    pd.DataFrame(data=base_embeddings.numpy(), index=countries).to_csv("embeddings_countries.csv")
    pd.DataFrame(data=ape_embeddings.numpy(), index=countries).to_csv("ape_embeddings_countries.csv")


# save_embeddings()
triples = pd.read_csv("KGs/Countries-S3/train.txt",
                      sep="\s+",
                      header=None, usecols=[0, 1, 2],
                      names=['subject', 'relation', 'object'],
                      dtype=str)
"""


places_to_be_locatedin = set(triples[(triples["relation"] == "locatedin")]["object"].tolist())
"""

df_countries = pd.read_csv("embeddings_countries.csv", index_col=0)
df_ape_countries = pd.read_csv("ape_embeddings_countries.csv", index_col=0)

assert df_countries.index.tolist() == df_ape_countries.index.tolist()
all_items = df_countries.index.tolist()
labels = []
items_to_locates = dict()
for idx, i in enumerate(all_items):
    objects = triples[(triples["subject"] == i) & (triples["relation"] == "locatedin")]["object"].tolist()

    labels.extend(objects)
    items_to_locates[i] = objects

tsne = TSNE(n_components=2, random_state=0)
low_emb = tsne.fit_transform(df_countries.values)

labels = list(set(labels) - set(all_items))
# blue, green, red, cyan, magenta, yellow, black, and white;
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

label_to_color = {l: colors[i] for i, l in enumerate(labels)}

for k, v in label_to_color.items():
    items = triples[(triples["object"] == k) & (triples["relation"] == "locatedin")]["subject"].tolist()
    idx = [all_items.index(i) for i in items]
    pos = low_emb[idx]

    plt.scatter(pos[:, 0], pos[:, 1], label=k)

plt.legend()
plt.grid(True)
plt.show()

low_emb = tsne.fit_transform(df_ape_countries.values)
for k, v in label_to_color.items():
    items = triples[(triples["object"] == k) & (triples["relation"] == "locatedin")]["subject"].tolist()
    idx = [all_items.index(i) for i in items]
    pos = low_emb[idx]

    plt.scatter(pos[:, 0], pos[:, 1], label=k)

plt.legend()
plt.grid(True)
plt.show()

exit(1)

exit(1)
for i in range(len(low_emb)):
    print(names[i])
exit(1)
classes = {}
for idx, i in enumerate(names):
    objects = triples[(triples["subject"] == i) & (triples["relation"] == "locatedin")]["object"].tolist()

    for j in objects:
        if "americas" in j:
            classes[i] = "americas"
        elif "caribbean" in j:
            classes[i] = "americas"
        elif "europe" in j:
            classes[i] = "europe"
        elif "asia" in j:
            classes[i] = "asia"
        elif "oceania" in j:
            classes[i] = "oceania"
        elif "australia_and_new_zealand" in j:
            classes[i] = "oceania"
        elif "australia_and_new_zealand" in j:
            classes[i] = "oceania"

        elif "africa" in j:
            classes[i] = "africa"

        else:
            print(j)
            exit(1)

        break

for k, v in classes.items():
    print(k, v)

plt.scatter(x=low_emb[:, 0], y=low_emb[:, 1], c=[classes[names[idx]] for idx in range(len(low_emb))])
plt.show()

df_ape = pd.read_csv("ape_embeddings_countries.csv", index_col=0)

tsne = TSNE(n_components=2, random_state=0)
low_emb = tsne.fit_transform(df_ape.values)
plt.scatter(x=low_emb[:, 0], y=low_emb[:, 1])
plt.show()

exit(1)


def save_analysis():
    triples = pd.read_csv("KGs/Countries-S3/train.txt",
                          sep="\s+",
                          header=None, usecols=[0, 1, 2],
                          names=['subject', 'relation', 'object'],
                          dtype=str).values.tolist()
    # print(set(triples[triples.relation=="locatedin"]["object"].tolist()))
    where_to_be_located = sorted(
        {'micronesia', 'middle_africa', 'northern_america', 'oceania', 'asia', 'caribbean', 'south-eastern_asia',
         'southern_africa', 'western_africa', 'southern_asia', 'polynesia', 'eastern_europe', 'northern_africa',
         'western_asia', 'central_europe', 'central_america', 'south_america', 'western_europe',
         'australia_and_new_zealand', 'southern_europe', 'europe', 'americas', 'africa', 'eastern_asia',
         'northern_europe', 'central_asia', 'melanesia', 'eastern_africa'})

    all_entities = set()
    for triple in triples:
        all_entities.add(triple[0])
        all_entities.add(triple[2])
    all_entities = list(all_entities)

    base_model = KGE("Experiments/2023-10-31 14-54-28.221507")
    attentive_bpe_model = KGE("Experiments/2023-10-31 14-56-38.631855")
    r = "locatedin"

    results = []
    abpe_results = []
    for h in all_entities:
        score = []
        abp_score = []
        for t in where_to_be_located:
            score.append(float(base_model.predict(h=h, r=r, t=t)))
            abp_score.append(float(attentive_bpe_model.predict(h=h, r=r, t=t)))
        results.append(score)
        abpe_results.append(abp_score)

    df_base = pd.DataFrame(results, index=all_entities, columns=where_to_be_located)
    abpe_results = pd.DataFrame(abpe_results, index=all_entities, columns=where_to_be_located)
    df_base.to_csv("base_analysis.csv")
    abpe_results.to_csv("abp_analysis.csv")


save_analysis()

df = pd.read_csv("base_analysis.csv", index_col=0)
abpe_df = pd.read_csv("abp_analysis.csv", index_col=0)

print(df.head())
print(abpe_df.head())
# western_europe

print(df[df["western_europe"] >= 0.60])
print(abpe_df[abpe_df["western_europe"] >= 0.60])
"""
BPE CODE
import re, collections


def get_stats(vocab):
    pairs = collections.defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[symbols[i], symbols[i + 1]] += freq
    return pairs


def merge_vocab(pair, v_in):
    v_out = {}
    bigram = re.escape(' '.join(pair))
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in v_in:
        w_out = p.sub(''.join(pair), word)
        v_out[w_out] = v_in[word]
    return v_out


vocab = {'l o w </w>': 5, 'l o w e r </w>': 2,
         'n e w e s t </w>': 6, 'w i d e s t </w>': 3}
num_merges = 10
for i in range(num_merges):
    pairs = get_stats(vocab)
    best = max(pairs, key=pairs.get)
    vocab = merge_vocab(best, vocab)
    print(best)


"""

import re, collections


def get_stats(vocab):
    pairs = collections.defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[symbols[i], symbols[i + 1]] += freq
    return pairs


def merge_vocab(pair, v_in):
    v_out = {}
    bigram = re.escape(' '.join(pair))
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in v_in:
        w_out = p.sub(''.join(pair), word)
        v_out[w_out] = v_in[word]
    return v_out


vocab = {'l o w </w>': 0, 'l o w e r </w>': 1,
         'n e w e s t </w>': 2, 'w i d e s t </w>': 3}
print(vocab)
num_merges = 10
for i in range(num_merges):
    pairs = get_stats(vocab)
    best = max(pairs, key=pairs.get)
    vocab = merge_vocab(best, vocab)
    print(best)

print(vocab)

exit(1)
from dicee import KGE
from dicee.config import Namespace

# KGE becomes LLM
pre_trained_kge = KGE(path="Experiments/2023-10-27 11-45-58.682971")
print(pre_trained_kge.predict(h="alga", r="isa", t="entity"))  # tensor([0.6932])
print(pre_trained_kge.predict(h="Demir", r="loves", t="Embeddings"))  # tensor([0.5593])
print(pre_trained_kge.predict(h="We", r="love", t="machine learning"))  # tensor([0.5008])
"""
*** Save Trained Model ***
Took 0.0098 secs | Current Memory Usage  693.89 in MB
Total Runtime: 95.928 seconds
Evaluate Keci on BPE Train set: Evaluate Keci on BPE Train set
{'H@1': 0.8173888036809815, 'H@3': 0.9484279141104295, 'H@10': 0.986579754601227, 'MRR': 0.8862843213146364}
Evaluate Keci on BPE Validation set: Evaluate Keci on BPE Validation set
{'H@1': 0.6802147239263804, 'H@3': 0.8688650306748467, 'H@10': 0.9493865030674846, 'MRR': 0.7841710119619227}
Evaluate Keci on BPE Test set: Evaluate Keci on BPE Test set
{'H@1': 0.680786686838124, 'H@3': 0.8789712556732224, 'H@10': 0.959909228441755, 'MRR': 0.7868645835207091}
Total Runtime: 97.860 seconds
"""

pre_trained_kge = KGE(path="Experiments/2023-10-27 11-48-12.795328")
print(pre_trained_kge.predict(h="alga", r="isa", t="entity"))  # tensor([0.7311])
print(pre_trained_kge.predict(h="Demir", r="loves", t="Embeddings"))
print(pre_trained_kge.predict(h="We", r="love", t="machine learning"))
"""
Training Runtime: 1.061 minutes.

*** Save Trained Model ***
Took 0.0016 secs | Current Memory Usage  653.01 in MB
Total Runtime: 64.356 seconds
Evaluate Keci on Train set: Evaluate Keci on Train set
{'H@1': 0.977760736196319, 'H@3': 0.9996165644171779, 'H@10': 1.0, 'MRR': 0.9886576102833773}
Evaluate Keci on Validation set: Evaluate Keci on Validation set
{'H@1': 0.5475460122699386, 'H@3': 0.8029141104294478, 'H@10': 0.9348159509202454, 'MRR': 0.6927008715144419}
Evaluate Keci on Test set: Evaluate Keci on Test set
{'H@1': 0.5642965204236006, 'H@3': 0.8040847201210287, 'H@10': 0.9440242057488654, 'MRR': 0.7044419021646735}
Total Runtime: 65.931 seconds

"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
import seaborn as sns

# sns.set(style="whitegrid")
pd.set_option('display.max_columns', None)

directory = "UMLS"
sub_folder_str_paths = os.listdir(directory)


def get_summaries(sub_folder_str_paths):
    summaries = []
    for i in sub_folder_str_paths:
        if i == "summary.csv":
            df = pd.read_csv(f"{directory}/{i}", index_col=0)
            summaries.append(df)

    df = pd.concat(summaries)

    df.sort_values(by=['test_mrr'], ascending=False, inplace=True)

    df["model_name"] = df["model_name"].str.replace("Pykeen_QuatE", "QuatE")
    df["model_name"] = df["model_name"].str.replace("Pykeen_TransE", "TransE")
    return df


df = get_summaries(sub_folder_str_paths)
conditions = [
    (df['callbacks'] == "{}"),
    (df['callbacks'].str.contains("'level': 'input'")),
    (df['callbacks'].str.contains("'level': 'param'")),
    (df['callbacks'].str.contains("'level': 'out'")),
]

values = ["Base", "Input", "Param", "Out"]

# create a new column and use np.select to assign values to it using our lists as arguments
df["label"] = np.select(conditions, values)

sub_df = df[["model_name", "train_mrr", "test_mrr", "callbacks", "label"]]

sns.boxplot(data=sub_df, x="label", y="test_mrr", order=values)
ax = sns.swarmplot(data=sub_df, x="label", y="test_mrr",  # hue="model_name",
                   order=values, c="black")
# remove legend from axis 'ax'
# ax.legend_.remove()
plt.ylim(0.0, 1.1)
plt.xlabel("")
plt.ylabel("MRR")
plt.title("Test MRR performances")
plt.savefig('test_robust.pdf')
plt.show()

sns.boxplot(data=sub_df, x="label", y="train_mrr", order=values)
ax = sns.swarmplot(data=sub_df, x="label", y="train_mrr",  # hue="model_name",
                   order=values, c="black")
# remove legend from axis 'ax'
# ax.legend_.remove()
plt.ylim(0.0, 1.1)
plt.xlabel("")
plt.ylabel("MRR")
plt.title("Train MRR performances")
plt.savefig('train_robust.pdf')
plt.show()
exit(1)

test_kge_mrr = sub_df[sub_df["label"] == "Base"]["test_mrr"].to_numpy()

test_kge_in_perturb = sub_df[sub_df["label"] == "Input"]["test_mrr"].to_numpy()
test_kge_param_perturb = sub_df[sub_df["label"] == "Param"]["test_mrr"].to_numpy()
test_kge_out_perturb = sub_df[sub_df["label"] == "Out"]["test_mrr"].to_numpy()

# Multiple box plots on one Axes
# fig, ax = plt.subplots()

# ax = sns.boxplot(x="day", y="total_bill", data=tips, showfliers = False)
# ax = sns.swarmplot(x="day", y="total_bill", data=tips, color=".25")

ax = sns.boxplot(data=[test_kge_mrr, test_kge_in_perturb, test_kge_param_perturb, test_kge_out_perturb],
                 # order=["Base", "Input", "Param", "Out"]
                 )
print(ax)
ax = sns.swarmplot(data=[test_kge_mrr, test_kge_in_perturb, test_kge_param_perturb, test_kge_out_perturb],
                   color=".25"
                   # labels=["Base", "Input", "Param", "Out"],
                   )
# fig.supylabel('Test MRR')
# plt.savefig('test_robust.pdf')
plt.show()
exit(1)
fig, ax = plt.subplots()
ax.boxplot([train_kge_mrr, train_kge_in_perturb, train_kge_param_perturb, train_kge_out_perturb], sym='gD',
           labels=["Base", "Input", "Param", "Out"])
fig.supylabel('Train MRR')
plt.savefig('train_robust.pdf')
plt.show()
exit(1)

# Fixing random state for reproducibility
np.random.seed(19680801)

# fake up some data
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))
"""
fig, axs = plt.subplots(2, 3)

# basic plot
axs[0, 0].boxplot(data)
axs[0, 0].set_title('basic plot')

# notched plot
axs[0, 1].boxplot(data, 1)
axs[0, 1].set_title('notched plot')

# change outlier point symbols
axs[0, 2].boxplot(data, 0, 'gD')
axs[0, 2].set_title('change outlier\npoint symbols')

# don't show outlier points
axs[1, 0].boxplot(data, 0, '')
axs[1, 0].set_title("don't show\noutlier points")

# horizontal boxes
axs[1, 1].boxplot(data, 0, 'rs', 0)
axs[1, 1].set_title('horizontal boxes')

# change whisker length
axs[1, 2].boxplot(data, 0, 'rs', 0, 0.75)
axs[1, 2].set_title('change whisker length')

fig.subplots_adjust(left=0.08, right=0.98, bottom=0.05, top=0.9,
                    hspace=0.4, wspace=0.3)
"""

# fake up some more data
spread = np.random.rand(50) * 100
center = np.ones(25) * 40
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
d2 = np.concatenate((spread, center, flier_high, flier_low))
# Making a 2-D array only works if all the columns are the
# same length.  If they are not, then use a list instead.
# This is actually more efficient because boxplot converts
# a 2-D array into a list of vectors internally anyway.
data = [data, d2, d2[::2]]

# Multiple box plots on one Axes
fig, ax = plt.subplots()
ax.boxplot(data)

plt.show()
exit(1)

df = pd.read_csv("UMLS-ComplEx-Perturb/summary.csv", index_col=0)

print(df.head())
exit(1)

# https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

random_dists = ['Normal(1, 1)', 'Lognormal(1, 1)', 'Exp(1)', 'Gumbel(6, 4)',
                'Triangular(2, 9, 11)']
N = 500

norm = np.random.normal(1, 1, N)
logn = np.random.lognormal(1, 1, N)
expo = np.random.exponential(1, N)
gumb = np.random.gumbel(6, 4, N)
tria = np.random.triangular(2, 9, 11, N)

# Generate some random indices that we'll use to resample the original data
# arrays. For code brevity, just use the same random indices for each array
bootstrap_indices = np.random.randint(0, N, N)
data = [
    norm, norm[bootstrap_indices],
    logn, logn[bootstrap_indices],
    expo, expo[bootstrap_indices],
    gumb, gumb[bootstrap_indices],
    tria, tria[bootstrap_indices],
]

fig, ax1 = plt.subplots(figsize=(10, 6))
fig.canvas.manager.set_window_title('A Boxplot Example')
fig.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

bp = ax1.boxplot(data, notch=False, sym='+', vert=True, whis=1.5)
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')

# Add a horizontal grid to the plot, but make it very light in color
# so we can use it for reading data values but not be distracting
ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

ax1.set(
    axisbelow=True,  # Hide the grid behind plot objects
    title='Comparison of IID Bootstrap Resampling Across Five Distributions',
    xlabel='Distribution',
    ylabel='Value',
)

# Now fill the boxes with desired colors
box_colors = ['darkkhaki', 'royalblue']
num_boxes = len(data)
medians = np.empty(num_boxes)
for i in range(num_boxes):
    box = bp['boxes'][i]
    box_x = []
    box_y = []
    for j in range(5):
        box_x.append(box.get_xdata()[j])
        box_y.append(box.get_ydata()[j])
    box_coords = np.column_stack([box_x, box_y])
    # Alternate between Dark Khaki and Royal Blue
    ax1.add_patch(Polygon(box_coords, facecolor=box_colors[i % 2]))
    # Now draw the median lines back over what we just filled in
    med = bp['medians'][i]
    median_x = []
    median_y = []
    for j in range(2):
        median_x.append(med.get_xdata()[j])
        median_y.append(med.get_ydata()[j])
        ax1.plot(median_x, median_y, 'k')
    medians[i] = median_y[0]
    # Finally, overplot the sample averages, with horizontal alignment
    # in the center of each box
    ax1.plot(np.average(med.get_xdata()), np.average(data[i]),
             color='w', marker='*', markeredgecolor='k')

# Set the axes ranges and axes labels
ax1.set_xlim(0.5, num_boxes + 0.5)
top = 40
bottom = -5
ax1.set_ylim(bottom, top)
ax1.set_xticklabels(np.repeat(random_dists, 2),
                    rotation=45, fontsize=8)

# Due to the Y-axis scale being different across samples, it can be
# hard to compare differences in medians across the samples. Add upper
# X-axis tick labels with the sample medians to aid in comparison
# (just use two decimal places of precision)
pos = np.arange(num_boxes) + 1
upper_labels = [str(round(s, 2)) for s in medians]
weights = ['bold', 'semibold']
for tick, label in zip(range(num_boxes), ax1.get_xticklabels()):
    k = tick % 2
    ax1.text(pos[tick], .95, upper_labels[tick],
             transform=ax1.get_xaxis_transform(),
             horizontalalignment='center', size='x-small',
             weight=weights[k], color=box_colors[k])

# Finally, add a basic legend
fig.text(0.80, 0.08, f'{N} Random Numbers',
         backgroundcolor=box_colors[0], color='black', weight='roman',
         size='x-small')
fig.text(0.80, 0.045, 'IID Bootstrap Resample',
         backgroundcolor=box_colors[1],
         color='white', weight='roman', size='x-small')
fig.text(0.80, 0.015, '*', color='white', backgroundcolor='silver',
         weight='roman', size='medium')
fig.text(0.815, 0.013, ' Average Value', color='black', weight='roman',
         size='x-small')

plt.show()

exit(1)
