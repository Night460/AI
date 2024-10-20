# Function to calculate the posterior probability using Bayes' Theorem
def bayes_theorem(P_A_given_B, P_B, P_A):
    return (P_A_given_B * P_B) / P_A


# Given probabilities
P_S = 0.30  # Prior probability that an email is spam
P_NS = 0.70  # Prior probability that an email is not spam
P_A_given_S = 0.80  # Probability that the word "lottery" appears in a spam email
P_A_given_NS = 0.10  # Probability that the word "lottery" appears in a non-spam email

# Calculate P(A), the total probability of the word "lottery" appearing in any email
P_A = (P_A_given_S * P_S) + (P_A_given_NS * P_NS)

# Calculate P(S|A), the posterior probability that the email is spam given that it contains the word "lottery"
P_S_given_A = bayes_theorem(P_A_given_S, P_S, P_A)

# Output the result
print(f"The probability that the email is spam given it contains the word 'lottery' is: {P_S_given_A:.4f}")