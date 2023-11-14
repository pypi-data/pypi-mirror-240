import numpy as np

def estimate_coef(x, y):
    n = np.size(x)
    m_x = np.mean(x)
    m_y = np.mean(y)
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x
    return (b_0, b_1)

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def main():
    # Read data from a CSV file
    filename = 'data1.csv'  # Replace with your CSV file path
    data = np.genfromtxt(filename, delimiter=',')

    x = data[:, 0]
    y = data[:, 1]

    b = estimate_coef(x, y)
    y_pred = b[0] + b[1] * x
    mse = mean_squared_error(y, y_pred)
    print("Estimated coefficients:\nb_0 = {}\nb_1 = {}".format(b[0], b[1]))
    print("Mean Squared Error (MSE):", mse)

    while True:
        user_x = float(input("Enter a value of x to predict y (or type 'exit' to quit): "))
        if user_x == 'exit':
            break
        user_y = b[0] + b[1] * user_x
        print("Predicted y:", user_y)

if __name__ == "__main__":
    main()
