# Import required libraries
import tensorflow as tf
import matplotlib.pyplot as plt
from tqdm import tqdm


def testing_run(assets=None, model=None, test_data=None):

    predictions = []

    for i, row in tqdm(enumerate(test_data)):

        prediction = tf.round(
            model.predict(
                tf.expand_dims(row, 0),
                verbose=0
            )
        ).numpy()
        predictions.append(prediction[0][0])

        if prediction == 1:  # 'Buy' branch
            if len(predictions) > 1 and predictions[i-1] == 1:
                pass
            else:
                assets.buy(open_price=row[4, 0].numpy())

        else:  # 'Sell' branch
            if len(predictions) > 1 and predictions[i-1] == 0:
                pass
            else:
                assets.sell(close_price=row[4, 3].numpy())
            pass

    assets.closure(close_price=row[4, 3].numpy())

    return predictions


def plot_testing_run(assets=None):

    shares_history = assets.shares_history
    money_history = assets.money_history

    plt.figure(figsize=(13, 7))
    plt.suptitle('Backtesting Results')

    plt.subplot(2, 1, 1)
    plt.plot(money_history, marker='o')

    plt.title('Money volume over time')
    plt.xlabel('No. of buy transactions')
    plt.ylabel('Money')

    plt.subplot(2, 1, 2)
    plt.plot(shares_history, marker='o')

    plt.title('Shares owned over time')
    plt.xlabel('No. of buy transactions')
    plt.ylabel('Shares')

    plt.show()

    pass
