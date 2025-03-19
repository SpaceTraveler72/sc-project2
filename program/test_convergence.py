import numpy as np

class ConvergenceClassifier:
    @staticmethod
    def classify_convergence(history):
        # Use the last 10 iterations for better accuracy
        history = history[2:]
        if len(history) < 3:
            return "Insufficient data to classify convergence", None

        errors = [abs(history[i+1] - history[i]) for i in range(len(history) - 1)]
        log_ratios = [np.log(errors[i+1]) / np.log(errors[i]) for i in range(len(errors) - 1) if errors[i] > 0 and errors[i+1] > 0]

        avg_lr = np.mean(log_ratios) if log_ratios else None

        if avg_lr is not None and avg_lr >= 2:
            return "Quadratic convergence", avg_lr
        elif avg_lr is not None and 1 < avg_lr < 2:
            return "Superlinear convergence", avg_lr
        elif avg_lr is not None and avg_lr <= 1:
            return "Linear convergence", avg_lr
        else:
            return "Unknown convergence type", avg_lr

    @staticmethod
    def test_convergence(results):
        with open("program/convergence_results.txt", "w") as file:
            for name, history_bisection, history_newton, history_secant in results:
                file.write(f"\nTesting convergence for {name}:\n")
                if history_bisection:
                    convergence_type, avg_lr = ConvergenceClassifier.classify_convergence(history_bisection)
                    file.write(f"Bisection method: {convergence_type} (Avg lr: {avg_lr})\n")
                if history_newton:
                    convergence_type, avg_lr = ConvergenceClassifier.classify_convergence(history_newton)
                    file.write(f"Newton's method: {convergence_type} (Avg lr: {avg_lr})\n")
                if history_secant:
                    convergence_type, avg_lr = ConvergenceClassifier.classify_convergence(history_secant)
                    file.write(f"Secant method: {convergence_type} (Avg lr: {avg_lr})\n")
