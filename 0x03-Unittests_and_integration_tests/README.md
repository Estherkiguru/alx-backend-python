0x03. Unittests and Integration Tests

This project involves creating unit and integration tests for various Python functions and classes. The tasks cover parameterization, exception handling, mocking, and integration testing.

Tasks
Parameterize a Unit Test

Write unit tests for the access_nested_map function using @parameterized.expand.
Parameterize a Unit Test with Exceptions

Extend tests for access_nested_map to check for KeyError exceptions using assertRaises and @parameterized.expand.
Mock HTTP Calls

Test the get_json function by mocking requests.get with unittest.mock.patch.
Parameterize and Patch Decorators

Test the memoize decorator to ensure the decorated function a_method is called only once.
Mocking a Property

Unit-test GithubOrgClient._public_repos_url by mocking GithubOrgClient.org.
More Patching

Test GithubOrgClient.public_repos by mocking get_json and _public_repos_url.
Parameterize with License Checking

Test GithubOrgClient.has_license by parameterizing the test for different license keys.
Integration Test with Fixtures

Test GithubOrgClient.public_repos method in an integration context using fixtures and @parameterized_class.
