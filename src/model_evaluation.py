from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_metrics(y_true, y_pred):
    """Calculate various model evaluation metrics."""
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    rmse = mean_squared_error(y_true, y_pred, squared=False)
    
    return {
        "MSE": mse,
        "R2 Score": r2,
        "MAE": mae,
        "RMSE": rmse
    }

def plot_predictions(y_true, y_pred, title):
    """Plot actual vs predicted values."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=range(len(y_true)), y=y_true, color='orange', label='Actual')
    sns.scatterplot(x=range(len(y_pred)), y=y_pred, color='purple', label='Predicted')
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Charges")
    plt.legend()
    plt.show()

def plot_correlation_heatmap(df_corr):
    """Plot correlation heatmap."""
    plt.figure(figsize=(8, 8))
    sns.heatmap(df_corr, annot=True, fmt='.2f', cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()

def compare_models(models_metrics):
    """Compare different models based on their metrics."""
    return pd.DataFrame(models_metrics).sort_values(by="R2 Score", ascending=False)
