from setuptools import setup, find_packages


VERSION = '1.1.1'
DESCRIPTION = 'Powerful data structures for data analysis, time series for information diffusion analysis'
LONG_DESCRIPTION = '''The proposed package is designed to facilitate comprehensive work on information diffusion analysis. 
It provides a versatile set of tools and functionalities that empower users to explore, model, and analyze the intricate dynamics 
of information spread within a given system.

Following is a sample scenario.

def measure_information_diffusion(posts, threshold):
    # Sort the set of posts . This should using  timestamps
    posts = sorted(posts, key=lambda x: x.timestamp)

    # Initialize empty set of trees
    trees = set()

    # Iterate over each post in the sorted set
    for i, p_i in enumerate(posts):
        # Initialize a new tree with a single node representing (p_i)
        T_i = {p_i}

        # For each post with a timestamp later than p_i
        for j in range(i + 1, len(posts)):
            p_j = posts[j]

            # Compute the similarity between the tags of p_i and p_j
            similarity = compute_similarity(p_i, p_j)

            # If similarity is above the threshold, add a directed edge from p_i to p_j in T_i
            if similarity > threshold:
                T_i.add(p_j)

            # If p_j has already been added to a diffusion tree in trees, merge T_i with that tree
            for T_j in trees:
                if p_j in T_j:
                    T_j.update(T_i)
                    break
            else:
                # If p_j hasn't been added to any diffusion tree, add T_i to trees
                trees.add(T_i)

    # Return the set of diffusion trees
    return trees




'''

# Setting up
setup(
    name="SMAdiffz",
    version=VERSION,
    author="H.M.M.Caldera",
    author_email="<maneeshac2020@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    keywords=['python', 'social media'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)