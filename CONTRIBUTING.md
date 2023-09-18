# Contribution Guide

Thank you for considering contributing to the `chatgptmax` project! We welcome your help in making this project even better. Below, you'll find guidelines on how to contribute effectively.

## How to Contribute

Contributing to `chatgptmax` is as simple as opening a Pull Request (PR) with your proposed changes. Here's how to do it:

1. **Fork the Repository**: Click the **Fork** button at the top right of the [GitHub repository](https://github.com/victoriadrake/chatgptmax/) to create your copy of the project.

2. **Clone Your Fork**: Clone your forked repository to your local machine.

   ```shell
   git clone https://github.com/your-username/chatgptmax.git
   cd chatgptmax
   ```

3. **Create a New Branch**: Create a new branch for your feature or bug fix.

   ```shell
   git checkout -b my-feature-branch
   ```

4. **Make Changes**: Make your desired changes to the codebase.

5. **Commit Changes**: Commit your changes with a descriptive commit message.

   ```shell
   git commit -m "Add new feature: my feature description"
   ```

6. **Push Changes**: Push your changes to your fork on GitHub.

   ```shell
   git push origin my-feature-branch
   ```

7. **Open a Pull Request (PR)**: Go to the [main repository](https://github.com/victoriadrake/chatgptmax/) and click the **New Pull Request** button. Choose the `master` branch as the base branch and your branch (`my-feature-branch`) as the compare branch. Describe your changes in detail and submit the PR.

## Coding Style

The `chatgptmax` project uses the [Black](https://black.readthedocs.io/en/stable/) code formatter for maintaining consistent code style and formatting. Please ensure that your code adheres to the formatting guidelines before submitting a PR.

You can run Black to format your code by installing it and running it on your changes:

```shell
pip install black
black .
```

## Testing

The project uses [Pytest](https://docs.pytest.org/en/6.2.x/) as the testing framework. If you're introducing new features or fixing bugs, we'd welcome corresponding tests to ensure that your changes work as expected. You can run the tests using the following command:

```shell
pytest
```

## Reporting Issues

If you encounter any issues or have suggestions for improvements, please open an issue in the GitHub repository. When reporting issues, provide as much detail as possible to help us understand and address the problem.

## Review Process

All contributions will be reviewed by project maintainers. During the review process, feedback may be provided, and changes may be requested. We appreciate your patience and willingness to improve the project.

## License

By contributing to this project, you agree that your contributions will be licensed under the [MIT License](LICENSE) that covers the `chatgptmax` project.

Thank you for contributing to `chatgptmax` and helping make it better for everyone!
