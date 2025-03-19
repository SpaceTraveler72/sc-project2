import numpy as np

class ConvergenceClassifier:
    @staticmethod
    def classify_convergence(history, real_root):
        # Use the last few iterations for better accuracy
        history = history[2:]
        if len(history) < 3:
            return "Insufficient data to classify convergence", None

        errors = [abs(x - real_root) for x in history]
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
            for name, history_bisection, history_newton, history_secant, real_root in results:
                file.write(f"\nTesting convergence for {name}:\n")
                if history_bisection:
                    convergence_type, avg_lr = ConvergenceClassifier.classify_convergence(history_bisection, real_root)
                    file.write(f"Bisection method: {convergence_type} (Avg lr: {avg_lr})\n")
                if history_newton:
                    convergence_type, avg_lr = ConvergenceClassifier.classify_convergence(history_newton, real_root)
                    file.write(f"Newton's method: {convergence_type} (Avg lr: {avg_lr})\n")
                if history_secant:
                    convergence_type, avg_lr = ConvergenceClassifier.classify_convergence(history_secant, real_root)
                    file.write(f"Secant method: {convergence_type} (Avg lr: {avg_lr})\n")
