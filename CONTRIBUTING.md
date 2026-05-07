# Contributing to Credit Card Fraud Detection

Thank you for your interest in contributing! This document provides guidelines to make the contribution process smooth and effective.

---

## 🐛 Reporting Bugs

1. Open an [issue](https://github.com/TUFAQUE/CREDIT-CARD-FRAUD-DETECTION-MODEL/issues) with a clear title.
2. Include:
   - A description of the expected vs. actual behavior.
   - Steps to reproduce the issue.
   - Your Python version, OS, and relevant library versions.
3. Add the `bug` label.

---

## 💡 Suggesting Enhancements

- Open an issue with the `enhancement` label.
- Describe the feature, its motivation, and an outline of the proposed implementation.

---

## 🔀 Pull Request Workflow

1. **Fork** the repository.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/<your-username>/CREDIT-CARD-FRAUD-DETECTION-MODEL.git
   ```
3. Create a **feature branch** from `main`:
   ```bash
   git checkout -b fix/your-fix-description
   ```
4. Make your changes and **commit** with clear messages:
   ```bash
   git commit -m "fix: short description of the fix"
   ```
5. **Push** the branch and open a Pull Request against `main`.

---

## ✅ Code Standards

| Area               | Guideline                                                 |
| ------------------- | --------------------------------------------------------- |
| **Python style**    | Follow [PEP 8](https://peps.python.org/pep-0008/)        |
| **Docstrings**      | Use [Google-style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) docstrings |
| **Commit messages** | Use [Conventional Commits](https://www.conventionalcommits.org/) (`fix:`, `feat:`, `docs:`, etc.) |
| **Dependencies**    | Add any new dependency to `requirements.txt`              |
| **Notebook cells**  | Keep outputs cleared before committing `.ipynb` files     |

---

## 📝 Commit Message Convention

```
<type>: <short summary>

[optional body — explain *why*, not *what*]
```

**Types:** `fix`, `feat`, `docs`, `refactor`, `test`, `chore`

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
