from typing import Callable

from faker import Faker

from authena_python_sdk.client import Client
from authena_python_sdk.models.user import User


def test_FUNC_client_user_filter_WITH_many_users_to_filter_all_EXPECT_users_found(
        sdk_client: Client,
        user_function: Callable[..., User],
        faker: Faker
) -> None:
    """
    Check whether all users can be retrieved.

    :param sdk_client: SDK client.
    :param user_function: User fixture.

    :return: No return.
    """
    # Create some random users.
    permissions = [faker.unique.word() for _ in range(3)]
    users = [user_function(permissions=permissions).username for _ in range(5)]

    # Try to filter all users.
    user_data = sdk_client.user.filter()

    # Check that all users were found.
    for username in users:
        assert user_data[username].username == username
        assert sorted(user_data[username].permissions) == sorted(permissions)
