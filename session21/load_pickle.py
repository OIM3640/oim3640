import pickle


with open("data/t.pkl", "rb") as file:
    t = pickle.load(file)

print(t)
