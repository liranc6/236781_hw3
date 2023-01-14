r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers


def part1_rnn_hyperparams():
    hypers = dict(
        batch_size=0,
        seq_len=0,
        h_dim=0,
        n_layers=0,
        dropout=0,
        learn_rate=0.0,
        lr_sched_factor=0.0,
        lr_sched_patience=0,
    )
    # TODO: Set the hyperparameters to train the model.
    # ====== YOUR CODE: ======
    hypers = dict(
        batch_size=256,
        seq_len=64,
        h_dim=512,
        n_layers=2,
        dropout=0.3,
        learn_rate=0.001,
        lr_sched_factor=0.45,
        lr_sched_patience=3,
    )
    # ========================
    return hypers


def part1_generation_params():
    start_seq = ""
    temperature = 0.5
    # TODO: Tweak the parameters to generate a literary masterpiece.
    # ====== YOUR CODE: ======
    start_seq = 'ACT I.'
    # ========================
    return start_seq, temperature


part1_q1 = r"""
**Your answer:**
"""

part1_q2 = r"""
**Your answer:**
"""

part1_q3 = r"""
**Your answer:**
"""

part1_q4 = r"""
**Your answer:**
"""
# ==============


# ==============
# Part 2 answers

PART2_CUSTOM_DATA_URL = None


def part2_vae_hyperparams():
    hypers = dict(
        batch_size=0, h_dim=0, z_dim=0, x_sigma2=0, learn_rate=0.0, betas=(0.0, 0.0),
    )
    # TODO: Tweak the hyperparameters to generate a former president.
    # ====== YOUR CODE: ======
    # ========================
    return hypers


part2_q1 = r"""
**Your answer:**

"""

part2_q2 = r"""
**Your answer:**

"""

part2_q3 = r"""
**Your answer:**

"""

part2_q4 = r"""
**Your answer:**

"""

# ==============

# ==============
# Part 3 answers




part3_q1 = r"""
**Your answer:**


"""

part3_q2 = r"""
**Your answer:**

"""

part3_q3 = r"""
**Your answer:**

"""

part3_q4 = r"""
**Your answer:**

"""


# ==============
