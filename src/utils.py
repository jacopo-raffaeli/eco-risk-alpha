import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(model, X, y, cv=5):
    # Fit on full dataset
    model.fit(X, y)
    y_pred_train = model.predict(X)
    train_rmse = np.sqrt(mean_squared_error(y, y_pred_train))
    train_r2   = r2_score(y, y_pred_train)

    # Fit with CV
    cv_scores = cross_val_score(model, X, y, cv=cv, scoring="neg_mean_squared_error")
    cv_rmse = np.sqrt(-cv_scores.mean())
    y_pred_cv = cross_val_predict(model, X, y, cv=cv)

    print(f"Train RMSE: {train_rmse:.2f}, R²: {train_r2:.2f}")
    print(f"CV RMSE: {cv_rmse:.2f}")

    plt.figure(figsize=(6,6))
    plt.scatter(y, y_pred_cv, alpha=0.5)
    plt.plot([min(y), max(y)], [min(y), max(y)], 'k--', lw=2)
    plt.xlabel("Actual CDS Spread (bps)")
    plt.ylabel("Predicted CDS Spread (bps)")
    plt.grid(True, alpha=0.5)
    plt.show()

def compute_cva(cds_spreads, discount_factors, expected_exposure, maturities, lgd):
    cds_spreads = cds_spreads
    cvas = []
    for cds in cds_spreads:
        cds = cds / 10000
        hazard_rate = cds / lgd
        survival_probs = np.exp(-hazard_rate * maturities)
        survival_probs = np.concatenate([[1], survival_probs])
        default_probs = survival_probs[:-1] - survival_probs[1:]
        cva = np.sum(discount_factors * expected_exposure * default_probs * lgd)
        cvas.append(cva)
    return np.array(cvas)
