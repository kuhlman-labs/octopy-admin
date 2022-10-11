# Contributing

Hi there! We're thrilled that you'd like to contribute to
this project. Your help is essential for keeping it great.

Contributions to this project are [released](https://help.github.com/articles/github-terms-of-service/#6-contributions-under-repository-license)
to the public under the [project's open source license](LICENSE).

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md).
By participating in this project you agree to abide by its terms.

## Submitting a pull request

1. Fork and clone the repository
2. Create a new branch: `git switch -C my-branch-name`
3. Make your changes, add tests, and make sure the tests still pass
4. Push to your fork and submit a pull request
5. Pat your self on the back and wait for your pull request to be reviewed and merged.

Here are a few things you can do that will increase the likelihood
of your pull request being accepted:

- Discuss your changes with the community in an issue.
- Allow your pull request to receive edits by maintainers.
- Keep your change as focused as possible.
- If there are multiple changes you would like to make that are not dependent
upon each other, consider submitting them as separate pull requests.
- Write a [good commit message](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).

## Local Development Setup

Once you have the repository cloned, there's a couple of additional
steps you'll need to take.

- If you haven't already, [create a GitHub organization you can use for testing](https://help.github.com/en/articles/creating-a-new-organization-from-scratch).
  - Optional: some may find it beneficial to create a test user
as well in order to avoid potential rate-limiting issues on your main account.
- If you haven't already, [generate a Personal Access Token (PAT) for authenticating.](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).
- Export the necessary configuration for authenticating with GitHub.
`GHE_HOSTNAME` is optional and only needed if you're using GitHub Enterprise.

  ```sh
  export API_TOKEN=<token used to authenticate>
  export GHE_HOSTNAME=<hostname of a GitHub Enterprise Server>
  ```

- Install Poetry

  ```sh
  pip install poetry
  ```

- Build the project dependencies

  ```sh
  poetry install
  ```

## Resources

- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [Using Pull Requests](https://help.github.com/articles/about-pull-requests/)
- [GitHub Help](https://help.github.com)
