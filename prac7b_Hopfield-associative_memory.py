import matplotlib.pyplot as plt
from neurodynex.hopfield_network import network, pattern_tools, plot_tools

# Parameters
pattern_size = 10  # Define the size of the patterns
nr_neurons = pattern_size ** 2

# Create an instance of the Hopfield network
hopfield_net = network.HopfieldNetwork(nr_neurons=nr_neurons)

# Instantiate a pattern factory
factory = pattern_tools.PatternFactory(pattern_size, pattern_size)

# Create a checkerboard pattern and a random pattern list
checkerboard = factory.create_checkerboard()
pattern_list = [checkerboard]
pattern_list.extend(factory.create_random_pattern_list(nr_patterns=3, on_probability=0.5))

# Plot the patterns
plot_tools.plot_pattern_list(pattern_list)

# Compute and plot the overlap matrix
overlap_matrix = pattern_tools.compute_overlap_matrix(pattern_list)
plot_tools.plot_overlap_matrix(overlap_matrix)

# Store patterns in the Hopfield network
hopfield_net.store_patterns(pattern_list)

# Create a noisy version of the checkerboard pattern
noisy_init_state = pattern_tools.flip_n(checkerboard, nr_of_flips=4)
hopfield_net.set_state_from_pattern(noisy_init_state)

# Run the Hopfield network with monitoring
states = hopfield_net.run_with_monitoring(nr_steps=4)

# Reshape the states into patterns
states_as_patterns = factory.reshape_patterns(states)

# Plot the state sequence and overlap
plot_tools.plot_state_sequence_and_overlap(
    states_as_patterns,
    pattern_list,
    reference_idx=0,
    suptitle="Network Dynamics"
)

# Show plots
plt.show()
