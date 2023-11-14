def defuzzy():
    s = """
    def center_of_sums_defuzzification(fuzzy_set):
        numerator = sum(x * fuzzy_set[x] for x in fuzzy_set)
        denominator = sum(fuzzy_set[x] for x in fuzzy_set)
        return numerator / denominator

    def center_of_gravity_defuzzification(fuzzy_set, step=1):
        numerator = sum(x * fuzzy_set[x] * step for x in fuzzy_set)
        denominator = sum(fuzzy_set[x] * step for x in fuzzy_set)
        return numerator / denominator

    def center_of_area_defuzzification(fuzzy_set, step=1):
        total_area = sum(fuzzy_set[x] * step for x in fuzzy_set)
        center_of_area = sum(x * fuzzy_set[x] * step for x in fuzzy_set) / total_area
        return center_of_area

    def weighted_average_defuzzification(fuzzy_set):
        numerator = sum(x * fuzzy_set[x] for x in fuzzy_set)
        denominator = sum(fuzzy_set[x] for x in fuzzy_set)
        return numerator / denominator

    def first_of_maxima_defuzzification(fuzzy_set):
        max_value = max(fuzzy_set.values())
        for x in fuzzy_set:
            if fuzzy_set[x] == max_value:
                return x

    def last_of_maxima_defuzzification(fuzzy_set):
        max_value = max(fuzzy_set.values())
        for x in reversed(sorted(fuzzy_set.keys())):
            if fuzzy_set[x] == max_value:
                return x

    def mean_of_maxima_defuzzification(fuzzy_set):
        max_values = [x for x, membership in fuzzy_set.items() if membership == max(fuzzy_set.values())]
        return sum(max_values) / len(max_values)

    fuzzy_set = {5: 0.8, 10: 0.4, 13: 0.5, 11: 0.2}
    print("Fuzzy Set: {", end="")
    for x, y in fuzzy_set.items():
        print(x, ":", y, end=" ")
    print("}", end="\n\n")

    crisp_value = center_of_sums_defuzzification(fuzzy_set)
    print("Crisp Value (Center of Sums):", round(crisp_value, 2))

    crisp_value = center_of_gravity_defuzzification(fuzzy_set, step=1)
    print("Crisp Value (Center of Gravity):", round(crisp_value, 2))

    crisp_value = center_of_area_defuzzification(fuzzy_set, step=1)
    print("Crisp Value (Center of Area):", round(crisp_value, 2))

    crisp_value = weighted_average_defuzzification(fuzzy_set)
    print("Crisp Value (Weighted Average):", round(crisp_value, 2))

    crisp_value = first_of_maxima_defuzzification(fuzzy_set)
    print("Crisp Value (First of Maxima):", round(crisp_value, 2))

    crisp_value = last_of_maxima_defuzzification(fuzzy_set)
    print("Crisp Value (Last of Maxima):", round(crisp_value, 2))

    crisp_value = mean_of_maxima_defuzzification(fuzzy_set)
    print("Crisp Value (Mean of Maxima):", round(crisp_value, 2))

    """
    print(s)


def fuzzyprimopp():
    s = """
    # Set
    A = dict()
    B = dict()
    Y = dict()

    A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
    B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}

    print('The First Fuzzy Set is :', A)
    print('The Second Fuzzy Set is :', B)

    # UNION
    A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
    B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}

    Y = {}

    for a, b in zip(A, B):
        Y[a] = max(A[a], B[b])
    print("Union: ", Y)

    # Intersection
    A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
    B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}

    Y = {}

    for a, b in zip(A, B):
        Y[a] = min(A[a], B[b])
    print("Union: ", Y)

    # Compliment
    A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
    Y = {}
    for a in A:
        Y[a] = 1 - A[a]
    print("Compliment: ", Y)

    # Subset
    a, b = 0, 0
    for A_key, B_key in zip(A, B):
        A_value = A[A_key]
        B_value = B[B_key]
        if A_value <= B_value:
            a += 1
        else:
            b += 1

    if a == 4:
        print('A is a subset of B')
    elif b == 4:
        print('B is a subset of A')
    else:
        print('A and B are independent')
    """
    print(s)


def som():
    s = """
    pip install minisom
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.preprocessing import LabelEncoder
    from minisom import MiniSom
    from sklearn.metrics import silhouette_score, davies_bouldin_score
    df = pd.read_csv("HR Data.csv")
    df
    df.isnull().sum()
    le = LabelEncoder()
    df['Departments'] = le.fit_transform(df['Departments'])
    df['salary'] = le.fit_transform(df['salary'])
    df = df.drop('left', axis=1)
    from sklearn.preprocessing import MinMaxScaler

    scaler = MinMaxScaler()
    X_norm = scaler.fit_transform(df)

    from minisom import MiniSom

    som = MiniSom(x=10, y=10, input_len=9, sigma=1.0, learning_rate=0.5, random_seed=42)
    som.random_weights_init(X_norm)
    som.train_random(data=X_norm, num_iteration=100)

    from sklearn.cluster import KMeans
    import matplotlib.pyplot as plt

    wcss = []

    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
        kmeans.fit(X_norm)
        wcss.append(kmeans.inertia_)

    plt.plot(range(1, 11), wcss)
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters')
    plt.ylabel('WCSS')
    plt.show()

    from minisom import MiniSom
    from sklearn.metrics import silhouette_score
    from sklearn.metrics import silhouette_score as sil_score
    import numpy as np

    silhouette_scores = []
    for n_clusters in range(2, 7):
        som = MiniSom(x=8, y=8, input_len=df.shape[1], sigma=1.0, learning_rate=0.5, random_seed=42)
        som.random_weights_init(df.values)
        som.train_random(data=df.values, num_iteration=100)
        neuron_indices = np.array([som.winner(x) for x in df.values])
        cluster_labels = [np.where((neuron_indices == neuron_idx).all(axis=1))[0][0] for neuron_idx in neuron_indices]
        sil_score_value = sil_score(df, cluster_labels)
        silhouette_scores.append(sil_score_value)

    optimal_n_clusters = np.argmax(silhouette_scores) + 2
    print('Optimal number of clusters:', optimal_n_clusters)

    pip install scikit-fuzzy

    import numpy as np
    import skfuzzy as fuzz

    data_matrix = df
    n_clusters = 2

    cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(data_matrix.T, n_clusters, m=2, error=0.005, maxiter=1000)

    partition_coef = sum((u ** 2).sum(axis=1)) / len(data_matrix)

    class_entropy = (-u * np.log(u)).sum() / len(data_matrix)

    print("Partition Coefficient: ", partition_coef)
    print("Classification Entropy: ", class_entropy)

    import numpy as np
    import skfuzzy as fuzz
    import matplotlib.pyplot as plt

    data_matrix = df.values

    for n_clusters in range(2, 6):

        fpc = fuzz.cluster.cmeans(data_matrix.T, n_clusters, m=2, error=0.005, maxiter=1000)

        print("Number of clusters:", n_clusters)
        print("Cluster Centroids:", cntr)

        plt.scatter(data_matrix[:, 0], data_matrix[:, 1], c=u.argmax(axis=0))
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.show()

        partition_coef = sum((u ** 2).sum(axis=1)) / len(data_matrix)
        class_entropy = (-u * np.log(u)).sum() / len(data_matrix)
        print("Partition Coefficient: ", partition_coef)
        print("Classification Entropy: ", class_entropy)

        print()
        print()
    """
    print(s)


def mlp():
    s = """
    import pandas as pd
    import numpy as np
    df=pd.read_csv("SOLARR.csv")
    df
    from sklearn.model_selection import train_test_split
    X = df.drop("Solar Radiation", axis=1)
    y = df["Solar Radiation"]

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25, random_state=42)
    from sklearn.neural_network import MLPRegressor
    mlp = MLPRegressor(hidden_layer_sizes=(100, 100), max_iter=1000, random_state=42)

    mlp.fit(X_train, y_train)
    import matplotlib.pyplot as plt

    plt.plot(mlp.loss_curve_,color='green')
    plt.xlabel('Number of iterations')
    plt.ylabel('Training Error')
    plt.show()

    from sklearn.metrics import mean_squared_error, mean_absolute_error
    y_pred = mlp.predict(X_test)

    rmse = mean_squared_error(y_test, y_pred, squared=False)
    mae = mean_absolute_error(y_test, y_pred)

    print("RMSE:", rmse)
    print("MAE:", mae)

    from sklearn.model_selection import GridSearchCV

    param_grid = {
        'hidden_layer_sizes': [(100,), (50, 50)],
        'activation': ['relu', 'tanh', 'logistic'],
        'alpha': [0.0001, 0.001, 0.01],
        'learning_rate_init': [0.001, 0.01, 0.1]
    }
    grid_search = GridSearchCV(mlp, param_grid=param_grid, cv=5, n_jobs=-1)
    grid_search.fit(X_train, y_train)

    print("Best parameters: ", grid_search.best_params_)
    print("Best score: ", grid_search.best_score_)

    from sklearn.model_selection import RandomizedSearchCV
    from scipy.stats import randint, uniform
    param_dist = {
        'hidden_layer_sizes': [(100,), (50, 50)],
        'activation': ['relu', 'tanh', 'logistic'],
        'alpha': uniform(0.0001, 0.01),
        'learning_rate_init': uniform(0.001, 0.1)
    }

    random_search = RandomizedSearchCV(mlp, param_distributions=param_dist, cv=5, n_jobs=-1)


    random_search.fit(X_train, y_train)

    print("Best parameters: ", random_search.best_params_)
    print("Best score: ", random_search.best_score_)

    """
    print(s)

def slp():

    s = """
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import statistics as stat
    from sklearn.preprocessing import LabelEncoder
    df=pd.read_csv("tested.csv")
    df
    LE = LabelEncoder()
    for i in df.columns:
        if i in df.select_dtypes("object").columns:
            df[i] = LE.fit_transform(df[i])
    df.head(5)
    for i in df.columns:
    df[i].fillna(df[i].mean(), inplace = True)
    df.isnull().sum()
    input_Dimension = 11
    Weights = np.random.rand(input_dim)
    Weights = np.random.rand(input_Dimension)

    er =[]
    w = []
    l = [0,0.1,0.2]

    for i in l:
        learning_rate = i
        e =[]
        Training_Data = df.copy(deep=True)
        Expected_Output = Training_Data.Embarked
        Training_Data = Training_Data.drop(['Embarked'],axis = 1)
        Training_Data = np.asarray(Training_Data)
        Training_count = len(Training_Data[:, 0])

        for epoch in range(0,5):
            for datum in range(0, Training_count):
                Output_Sum = np.sum(np.multiply(Training_Data[datum, :], Weights))
                if Output_Sum < 0:
                    Output_Value = 0;
                else:
                    Output_Value = 1;
                error = Expected_Output[datum] - Output_Value
                e.append(error)
                for n in range(0, input_Dimension):
                    Weights[n] = Weights[n] + learning_rate * error * Training_Data[datum,n]
        er.append(e)
        w.append(Weights)

    min_er = []
    for i in er:
        c = 0
        for j in i:
            c += abs(j)
        min_er.append(c)

    for i in range(len(min_er)):
        if min_er[i] == min(min_er):
            #print(l[i])
            print(w[i])

    import matplotlib.pyplot as plt

    plt.plot(er[0])
    plt.show()
    plt.plot(er[1])
    plt.show()
    plt.plot(er[2])
    plt.show()
    """
    print(s)

def linreg1():

    s = """
    import pandas as pd
    import numpy as np
    data=pd.read_csv("Salary_dataset.csv")
    data

    print("before dropping: ",data.shape)

    print("Dropping Missing Values > 10%")
    print()

    df_len = len(data)
    mis_vals = {}

    drop_cols = []
    impt_cols = []

    for col in data.columns:
    percent = (data[col].isnull().sum()/df_len) * 100
    if percent > 10:
        drop_cols.append(col)
    elif percent > 0:
        impt_cols.append(col)

    mis_vals[col] = percent

    print(" Before drop : ",data.shape)
    data.drop(drop_cols,axis=1,inplace=True)
    print(" After  drop : ",data.shape)
    print()

    num , den = 0 , 0

    mean_x = X.mean()
    mean_y = Y.mean()

    for i , x in enumerate(X):
    y = Y[i]
    num += (x-mean_x) * (y-mean_y)
    den += (x-mean_x) ** 2

    b = num/den
    a = mean_y - (b * mean_x)

    print("bo : ",b," | b1 : ",a)
    pred = lambda x,a,b : a + (b * x)
    ssr = 0
    sst = 0

    mean_y = Y.mean()

    for i,y in enumerate(Y):
    x = X[i]
    ssr += ((y - pred(x,a,b)) ** 2)
    sst += (y - mean_y) ** 2

    print("rss : ",ssr)

    import math
    n    = len(Y)
    rmse = math.sqrt(ssr/n)

    print("rmse : ",rmse)

    import matplotlib.pyplot as plt
    plt.figure()
    plt.scatter(X, Y, color = 'green', alpha=0.5)

    plt_y = a + (b * np.linspace(0,10.0))
    plt.plot(np.linspace(0,10.0),plt_y, color = 'b')
    plt.xlabel("age")
    plt.ylabel("expenses")

    plt.show()
    """
    print(s)


def genetic():
    s = """import numpy as np
    import matplotlib.pyplot as plt

    # Fitness function
    def fitness(x):
        return 1+x**2

    # Initialization
    POP_SIZE = 150
    GENES = np.linspace(-10, 10, 1000)
    NUM_GENES = len(GENES)
    MUTATION_RATE = 0.01
    NUM_GENERATIONS = 75

    # Generate initial population
    population = np.random.choice(GENES, POP_SIZE)

    # Lists to store fitness data
    best_fitnesses = []
    avg_fitnesses = []
    worst_fitnesses = []

    # Selection function
    def select_parents(population):
        # Select two random individuals based on their fitness
        idx = np.random.choice(POP_SIZE, size=2, p=fitness(population) / fitness(population).sum())
        return population[idx[0]], population[idx[1]]

    # Crossover function
    def crossover(parent1, parent2):
        child = (parent1 + parent2) / 2
        return child

    # Mutation function
    def mutate(child):
        if np.random.rand() < MUTATION_RATE:
            mutation_value = np.random.choice(GENES)
            child = child + mutation_value
        return child

    # Main loop
    for generation in range(NUM_GENERATIONS):
        new_population = []
        for i in range(POP_SIZE):
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        population = np.array(new_population)
        best_individual = population[np.argmax(fitness(population))]

        # Update fitness lists
        best_fitnesses.append(fitness(best_individual))
        avg_fitnesses.append(np.mean(fitness(population)))
        worst_fitnesses.append(np.min(fitness(population)))

        print(f"Generation {generation + 1}: Best Value = {best_individual}, Fitness = {fitness(best_individual)}")

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(best_fitnesses, label="Best Fitness")
    plt.plot(avg_fitnesses, label="Average Fitness")
    plt.plot(worst_fitnesses, label="Worst Fitness")
    plt.xlabel("Generation")
    plt.ylabel("Fitness Value")
    plt.title("Evolution of Fitness over Generations")
    plt.axhline(y=fitness(best_individual), color='r', linestyle='--', label=f"Fitness of final best solution: {best_individual:.2f}")
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"Final best solution: {best_individual}")

    """
    print(s)

def mamdani():

    s = """import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('fan_speed_dataset.csv')

    def cold(temp):
        return max(0, min(1, (20 - temp) / 10))

    def medium(temp):
        return max(0, min(1, (temp - 10) / 10, (30 - temp) / 10))

    def hot(temp):
        return max(0, min(1, (temp - 20) / 10))

    def slow(speed):
        return max(0, min(1, (50 - speed) / 25))

    def med(speed):
        return max(0, min(1, (speed - 25) / 25, (75 - speed) / 25))

    def fast(speed):
        return max(0, min(1, (speed - 50) / 25))

    # Mamdani Fuzzy Inference System
    def mamdani_FIS(temp):
        # Rule Evaluation
        r1 = cold(temp)
        r2 = medium(temp)
        r3 = hot(temp)

        # Aggregation
        aggregated = [max(min(r1, slow(speed)), min(r2, med(speed)), min(r3, fast(speed))) for speed in range(101)]

        # Defuzzification (using centroid method)
        numerator = sum([speed * membership for speed, membership in enumerate(aggregated)])
        denominator = sum(aggregated)

        return numerator / denominator if denominator != 0 else 0

    # Apply the Mamdani FIS to the dataset
    df['Predicted Fan Speed'] = df['Temperature'].apply(mamdani_FIS)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Temperature'], df['Observed Fan Speed'], color='green', label='Observed Fan Speed', alpha=0.6)
    plt.plot(df['Temperature'], df['Predicted Fan Speed'], 'r-', label='Predicted Fan Speed')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Fan Speed (RPM)')
    plt.title('Observed vs. Predicted Fan Speed')
    plt.legend()
    plt.grid(True)
    plt.show()"""
    print(s)

def sugeno():
    s = """!pip install scikit-fuzzy
    import pandas as pd
    import numpy as np
    import skfuzzy as fuzz
    from skfuzzy import control as ctrl
    import matplotlib.pyplot as plt

    # Load dataset
    data_url = 'dataset.csv'
    data = pd.read_csv(data_url)

    # Define fuzzy variables
    temperature = ctrl.Antecedent(np.arange(0, 51, 1), 'temperature')
    humidity = ctrl.Antecedent(np.arange(0, 61, 1), 'humidity')
    output = ctrl.Consequent(np.arange(0, 26, 1), 'output', defuzzify_method='centroid')

    # Generate fuzzy membership functions
    temperature.automf(3)
    humidity.automf(3)
    output['low'] = fuzz.trimf(output.universe, [0, 5, 10])
    output['medium'] = fuzz.trimf(output.universe, [10, 15, 20])
    output['high'] = fuzz.trimf(output.universe, [15, 20, 25])

    # Define rules using Sugeno-type fuzzy inference
    rule1 = ctrl.Rule(temperature['poor'] & humidity['poor'], output['low'])
    rule2 = ctrl.Rule(temperature['average'] & humidity['average'], output['medium'])
    rule3 = ctrl.Rule(temperature['good'] & humidity['good'], output['high'])

    # Create control system
    output_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
    output_simulation = ctrl.ControlSystemSimulation(output_ctrl)

    # Simulation
    test_temp = 28
    test_humidity = 37

    output_simulation.input['temperature'] = test_temp
    output_simulation.input['humidity'] = test_humidity
    output_simulation.compute()

    print(f"For Temperature: {test_temp} and Humidity: {test_humidity}, the Output is: {output_simulation.output['output']}")

    # Plot membership functions and results
    temperature.view()
    humidity.view()
    output.view(sim=output_simulation)
    plt.show()"""
    print(s)



def PSO():

    s = """import numpy as np

    class Particle:
        def __init__(self, x0):
            self.position = np.array(x0)
            self.velocity = np.array([0.0] * len(x0))
            self.best_position = self.position.copy()
            self.best_fitness = float('inf')

        def update_position(self):
            self.position += self.velocity

        def update_velocity(self, global_best_position, w, c1, c2):
        r1 = np.random.rand(len(self.position))
        r2 = np.random.rand(len(self.position))

        if global_best_position is not None:
            self.velocity = (w * self.velocity) + (c1 * r1 * (self.best_position - self.position)) + (c2 * r2 * (global_best_position - self.position))
        else:
            # Handle the case when global_best_position is not set
            self.velocity = (w * self.velocity) + (c1 * r1 * (self.best_position - self.position))

        def evaluate_fitness(self, objective_function):
            self.fitness = objective_function(self.position)
            if self.fitness < self.best_fitness:
                self.best_fitness = self.fitness
                self.best_position = self.position.copy()

    def particle_swarm_optimization(objective_function, bounds, num_particles, max_iterations, w, c1, c2):
        particles = []

        global_best_position = None
        global_best_fitness = float('inf')

        # Initialize particles
        for _ in range(num_particles):
            x0 = []
            for bound in bounds:
                x0.append(np.random.uniform(bound[0], bound[1]))
            particle = Particle(x0)
            particles.append(particle)
            if particle.best_fitness < global_best_fitness:
                global_best_fitness = particle.best_fitness
                global_best_position = particle.best_position.copy()

        # Iterate for a given number of iterations
        for _ in range(max_iterations):
            for particle in particles:
                particle.update_velocity(global_best_position, w, c1, c2)
                particle.update_position()
                particle.evaluate_fitness(objective_function)
                if particle.best_fitness < global_best_fitness:
                    global_best_fitness = particle.best_fitness
                    global_best_position = particle.best_position.copy()

        return global_best_position, global_best_fitness


    def objective_function(x):
        return sum(x**2)

    bounds = [(-5, 5), (-5, 5), (-5, 5)]
    num_particles = 25
    max_iterations = 300
    w = 0.5
    c1 = 1.0
    c2 = 1.0

    best_position, best_fitness = particle_swarm_optimization(objective_function, bounds, num_particles, max_iterations, w, c1, c2)
    print("Best position:", best_position)
    print("Best fitness:", best_fitness)

    """
    print(s)

