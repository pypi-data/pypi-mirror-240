import gym
import numpy as np
import random
import scipy.linalg as la
from scipy.sparse.csgraph import connected_components

def get_communicating_classes(matrix):
    """ Finds the communicating classes in the Markov chain. """
    # Use scipy's connected_components to find the strongly connected components
    n_components, labels = connected_components(csgraph=matrix, directed=True, return_labels=True)
    
    # Create a list of lists to hold states for each communicating class
    classes = [[] for _ in range(n_components)]
    for index, label in enumerate(labels):
        classes[label].append(index)
    
    return classes

def get_stationary_distribution_for_class(matrix, communicating_class):
    """ Finds the stationary distribution for a communicating class. """
    # Extract the submatrix corresponding to the communicating class
    submatrix = matrix[communicating_class, :][:, communicating_class]
    
    # Number of states in the class
    n = len(submatrix)
    
    # Create an augmented matrix to account for the normalization condition
    # We stack an additional row for the constraint that probabilities sum to 1
    A = np.vstack((submatrix - np.eye(n), np.ones(n)))
    b = np.zeros(n + 1)
    b[-1] = 1  # The sum of the probabilities should be 1

    # Solve the system of linear equations
    pi, residuals, rank, s = la.lstsq(A.T, b)  # Transpose A to solve the left eigenvector problem

    # Return the stationary distribution for the class, with zero-padding for the other states
    full_pi = np.zeros(len(matrix))
    for i, state in enumerate(communicating_class):
        full_pi[state] = pi[i]

    return full_pi

def combine_distributions(distributions, weights):
    """ Combine distributions weighted by the size of each class. """
    combined_distribution = np.zeros_like(distributions[0])
    for dist, weight in zip(distributions, weights):
        combined_distribution += dist * weight
    return combined_distribution / combined_distribution.sum()

def analyze_markov_chain(matrix):
    """ Analyze the Markov chain to find the stationary distribution. """
    # Find the communicating classes
    classes = get_communicating_classes(matrix)
    
    # Handle the reducible case
    if len(classes) > 1:
        # Calculate the stationary distribution for each class
        distributions = [get_stationary_distribution_for_class(matrix, c) for c in classes]
        # Assuming a uniform initial distribution, the weight is the relative size of the class
        weights = [len(c) / len(matrix) for c in classes]
        # Combine the distributions
        return combine_distributions(distributions, weights)
    # Handle the irreducible case
    else:
        return get_stationary_distribution_for_class(matrix, classes[0])

def calculate_stationary_distribution(matrix, communicating_classes):
    """
    Calculates the stationary distribution for the entire Markov chain
    given the communicating classes and assuming a uniform initial distribution over states.
    """
    n = matrix.shape[0]  # Total number of states in the Markov chain
    uniform_initial_distribution = np.ones(n) / n  # Uniform distribution over states

    # Initialize the stationary distribution for the entire chain
    full_stationary_distribution = np.zeros(n)

    # Calculate the stationary distribution for each communicating class
    for states in communicating_classes:
        # Formulate the system πP = π
        submatrix = matrix[states][:, states]
        num_states_in_class = len(submatrix)
        A = np.vstack((submatrix.T - np.eye(num_states_in_class), np.ones(num_states_in_class)))
        b = np.zeros(num_states_in_class + 1)
        b[-1] = 1  # The sum of probabilities should be 1

        # Solve the system
        pi, _, _, _ = la.lstsq(A, b)

        # Assign the stationary distribution to the full distribution
        # weighted by the initial probability of the states in the class
        for i, state in enumerate(states):
            full_stationary_distribution[state] = pi[i] * (num_states_in_class / n)

    # Normalize the stationary distribution to ensure it sums to 1
    full_stationary_distribution /= full_stationary_distribution.sum()

    return full_stationary_distribution

class DiseaseTreatmentEnv(gym.Env):
    """Environment to model disease treatment using RL."""

    def __init__(self, 
                 n_diseases=3, 
                 n_treatments=5, 
                 n_symptoms=7, 
                 treatment_cost_range=(1, 5),
                 disease_cost_range=(1, 10), 
                 symptom_modulation_range=(-0.5, 0.25),
                 remission_reward=64,
                 seed=1,
                 max_visits=32,
                 use_gymnasium=False):
        super(DiseaseTreatmentEnv, self).__init__()

        # Create a non-defaut numpy rng
        rng = np.random.RandomState(seed)

        # Configurable parameters
        self.treatment_cost_range = treatment_cost_range
        self.disease_cost_range = disease_cost_range
        self.symptom_modulation_range = symptom_modulation_range
        self.remission_reward = remission_reward
        self.max_visits=max_visits

        # Step tracking
        self.visit_number = 0

        # Action and observation spaces
        if use_gymnasium:
            import gymnasium
            self.action_space = gymnasium.spaces.Discrete(n_treatments)
            self.observation_space = gymnasium.spaces.Box(low=0, high=1,
                 shape=(n_symptoms + n_treatments,), dtype=np.float32)
        else:
            self.action_space = gym.spaces.Discrete(n_treatments)
            self.observation_space = gym.spaces.Box(low=0, high=1,
                 shape=(n_symptoms + n_treatments,), dtype=np.float32)

        self.n_diseases = n_diseases
        self.n_treatments = n_treatments
        self.n_symptoms = n_symptoms

        self.connection_probability = 1 / n_diseases
        
        self.generate_diseases(rng)
        self.disease_list = list(self.diseases.keys())
        self.treatments = self.generate_treatments(rng)

        self.current_disease = None
        self.current_symptoms = np.zeros(n_symptoms)
        self.generate_transition_matrix(rng)
        self.compute_stationary_distribution()
        self.reset()

    def generate_transition_matrix(self, rng):
        # Initialize a matrix filled with zeros for off-diagonal elements, and ones on the diagonal
        self.transition_matrix = np.eye(self.n_diseases)
        
        for i in range(self.n_diseases):
            for j in range(self.n_diseases):
                if i != j:
                    if rng.rand() < self.connection_probability:  # Check for connection
                        # Transition probabilities between 1% to 20%
                        self.transition_matrix[i][j] = rng.uniform(0.01, 0.2)
                        self.transition_matrix[j][i] = rng.uniform(0.01, 0.2)

        # Normalize rows to sum to 1, representing probability distributions
        row_sums = self.transition_matrix.sum(axis=1) - 1  # Exclude self-transition in normalization
        self.transition_matrix[np.arange(self.n_diseases), np.arange(self.n_diseases)] = 1 - row_sums

    def compute_stationary_distribution(self):
        # Compute the stationary distribution for the Markov chain
        self.communicating_classes = get_communicating_classes(self.transition_matrix)
        self.stationary_distribution = calculate_stationary_distribution(self.transition_matrix, self.communicating_classes)

    def generate_diseases(self, rng):
        self.diseases = {}  # Initialize the dictionary
        for i in range(self.n_diseases):
            num_symptoms_for_disease = rng.randint(1, max(2, self.n_symptoms // 2))
            symptoms_for_disease = rng.choice(self.n_symptoms, size=num_symptoms_for_disease, replace=False)

            num_effective_treatments = rng.randint(1, max(2, self.n_treatments // 2))
            effective_treatments = rng.choice(self.n_treatments, size=num_effective_treatments, replace=False)
            
           
            means = rng.uniform(0.3, 0.7, size=num_symptoms_for_disease)  # Choosing values to make sure most symptoms stay within [0,1]
            std_devs = rng.uniform(0.05, 0.15, size=num_symptoms_for_disease)  # Small values to prevent wild swings in symptom values
            symptom_distributions = list(zip(means, std_devs))
 
            treatment_to_remission_probs = rng.uniform(0.1, 0.8, size=num_effective_treatments)
            
            base_reward = -rng.uniform(*self.disease_cost_range)

            self.diseases[f"Disease_{i}"] = {
                'symptoms': symptoms_for_disease,
                'treatments': effective_treatments,
                'symptom_distributions': symptom_distributions,
                'remission_probs': dict(zip(effective_treatments, treatment_to_remission_probs)),
                'base_reward': base_reward  # Assign base reward for the disease
            }

    def _combine(self, observation, action):
        """Combine the observation and action into a single vector
        action vector is one-hot encoded"""
        action_one_hot = np.zeros(self.n_treatments, dtype=np.float32)
        action_one_hot[int(action)] = 1.0
        return np.concatenate([observation, action_one_hot])

    def step(self, action):
        prev_disease = self.current_disease
        old_symptoms = self.current_symptoms.copy()
        self.visit_number += 1

        # Get the chosen treatment
        treatment = self.treatments[f"Treatment_{action}"]
        
        # Apply the treatment's base cost
        reward = -treatment['base_cost']

        # Check remission based on current disease and treatment
        remission_prob = self.diseases[self.current_disease]['remission_probs'].get(action, 0)

        # If remission occurs, update state and reward
        if np.random.rand() < remission_prob:
            self.current_disease = "Remission"
            #print("[DEBUG] Remission achieved!")
            reward += self.remission_reward
            self.current_symptoms = np.zeros(self.n_symptoms)  # Reset symptoms for remission
            return self._combine(self.current_symptoms, action), reward, True, {"treatment": action, "disease_pre_treatment": self.current_disease}

        # If remission doesn't occur, proceed with disease transition logic
        treatment_modifiers = treatment["transition_modifiers"]
        modified_transitions = self.transition_matrix[self.current_disease_index] * treatment_modifiers
        modified_transitions /= modified_transitions.sum()
        new_disease_index = np.random.choice(self.n_diseases, p=modified_transitions)
        self.current_disease = f"Disease_{new_disease_index}"
        self.current_disease_index = new_disease_index
        #print(f"[DEBUG] Previous disease: {prev_disease}, Applied treatment: {action}, New disease: {self.current_disease}")


        # Deduct the base reward for the current disease from the total reward
        reward += self.diseases[self.current_disease]['base_reward']

        # Fluctuate symptoms based on disease distributions and then adjust them based on treatment effects
        self.current_symptoms = self.sample_symptoms()
        for symptom, change in treatment['affected_symptoms'].items():
            self.current_symptoms[symptom] += change
        self.current_symptoms = np.clip(self.current_symptoms, 0, 1)

        # Visits cutoff
        terminated = self.visit_number == self.max_visits
            

        #if np.any(np.isnan(self.current_symptoms)) or np.any(self.current_symptoms < 0) or np.any(self.current_symptoms > 1):
            #print("[DEBUG] Invalid symptom values detected!", self.current_symptoms, "Old symptoms:", old_symptoms, "Applied treatment:", action)

        #print(f"[DEBUG] Obs: {self.current_symptoms}, Reward: {reward}, Treatment: {action}, Disease: {self.current_disease}")
        return self._combine(self.current_symptoms, action), reward, terminated, {"treatment": action, "disease_pre_treatment": self.current_disease}

    def sample_symptoms(self):
        symptom_values = np.zeros(self.n_symptoms)
        
        if self.current_disease == "Remission":
            return symptom_values  # No symptoms
        
        symptoms_for_disease = self.diseases[self.current_disease]['symptoms']
        symptom_distributions = self.diseases[self.current_disease]['symptom_distributions']
        
        for symptom, (mean, std_dev) in zip(symptoms_for_disease, symptom_distributions):
            sampled_value = np.random.normal(mean, std_dev)
            symptom_values[symptom] = sampled_value
        symptom_values = np.clip(symptom_values, 0, 1)

        return symptom_values
    
    def generate_treatments(self, rng):
        treatments = {}
        for i in range(self.n_treatments):
            # Each treatment can have a cost between the configurable range
            base_cost = rng.uniform(*self.treatment_cost_range)  
            
            affected_symptoms_count = rng.randint(1, max(2, self.n_symptoms // 2))
            affected_symptoms = rng.choice(self.n_symptoms, size=affected_symptoms_count, replace=False)
            
            # Change in symptom severity due to treatment is generated within the configurable range
            symptom_changes = {symptom: rng.uniform(*self.symptom_modulation_range) for symptom in affected_symptoms}
            
            treatments[f"Treatment_{i}"] = {
                'base_cost': base_cost,
                'affected_symptoms': symptom_changes
            }

            # Generate treatment-specific transition modifiers for each disease transition
            transition_modifiers = rng.uniform(0.5, 1.5, size=self.n_diseases)
            treatments[f"Treatment_{i}"]["transition_modifiers"] = transition_modifiers
        return treatments

    def reset(self, *, seed=None, options=None):
        self.current_disease = np.random.choice(self.disease_list, p=self.stationary_distribution)
        self.current_disease_index = self.disease_list.index(self.current_disease)
        self.current_symptoms = self.sample_symptoms()  # Initialize symptoms based on the current disease
        self.visit_number=0
        #print(f"[DEBUG] Resetting environment. Starting disease: {self.current_disease}, Initial symptoms: {self.current_symptoms}")
        return self._combine(self.current_symptoms, -1)
        

    def render(self, mode='human'):
        # Simple visualization for now
        print(f"Current Disease: {self.current_disease}")
        print(f"Current Symptoms: {self.current_symptoms}")
        print("\n")
