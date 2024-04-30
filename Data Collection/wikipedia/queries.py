"""
  --> contains sample queries, similar to britannicaScrapper
"""

class WikiQueries:
  def __init__(self):
    self.sample_queries = [
      "Antarctica",
      "Colonization",
      "World war",
      "Asia",
      "Africa",
      "Australia",
      "The holocaust",
      "Viruses",
      "Martin Luther King Jr",
      "Abraham Lincon",
      "Quarks",
      "Quantum mechanincs",
      "Drug",
      "Rocket",
      "Physics",
      "Mathematics",
      "Nuclear physics",
      "Nuclear fusion",
      "Nuclear fission",
      "CRISPR",
      "Virginia Woolf",
      "Cocaine", 
      "Marijuana",
      "Apollo program",
      "Birds",
      "Blog",
      "Journal",
      "Adolf Hitler",
      "Presidents of the United States",
      "Gender",
      "Journalism",
      "Matter",
      "Particle physics",
      "Particle accelerator",
      "Literature",
      "Wikipedia",
      "Loss function",
      "Bayesian probability",
    ]

  def __call__(self):
    return self.sample_queries