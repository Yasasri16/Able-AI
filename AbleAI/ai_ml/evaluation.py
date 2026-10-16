from sklearn.metrics import accuracy_score, classification_report

def evaluate_model(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    report = classification_report(y_true, y_pred)
    return accuracy, report

if __name__ == "__main__":
    # Example test
    y_true = [0, 1, 0, 1, 1]
    y_pred = [0, 1, 0, 0, 1]
    acc, rep = evaluate_model(y_true, y_pred)
    print("Accuracy:", acc)
    print("Classification Report:\n", rep)
