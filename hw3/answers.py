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
    hypers["betas"] = (0.99, 0.999)
    hypers["batch_size"] = 8
    hypers["h_dim"] = 800
    hypers["z_dim"] = 40
    hypers["x_sigma2"] = 0.002
    hypers["learn_rate"] = 0.0002
    # ========================
    return hypers


part2_q1 = r"""
**Your answer:**
Sigma controls the amount of regularization in the VAE.

A small sigma makes the loss more dependant on the difference between the original and reconstructed image.
A high sigma makes the loss more dependant on the kldiv loss, which encourages a smoother latent space.
Therefore, a larger sigma will limit the variety of generated samples' difference from one another, 
and a smaller sigma will give us more variety but images will make less sense. 

"""

part2_q2 = r"""
**Your answer:**
**1**
The reconstruction loss tries to create images which similar to the original given images, whereas
KL divergence loss tries to make sure the tow images  that are close on the latent space will reconstruct two similar images (smooth latent space).

**2**
The latent-space variance and the KL loss are directly proportional.
A smaller loss will minimize the variance of the latent space.

**3**
The benefit of this effect is that a smoother latent space will help the model generate two similar reconstructions for\
two similar input images. 

"""

part2_q3 = r"""
**Your answer:**
The number of possible options for a 3x64x64 image is very high, and we want our generated image to be near the space of real-data images.
Thus we need to increase the likelihood of generated images to be in the space of dataset images,
In order to do so we maximize our evidence probability.

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
