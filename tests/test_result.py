from tryon_service.core.result import Result


def test_success_result() -> None:
    result = Result.success(100)

    assert result.is_success
    assert result.value == 100
    assert result.error is None


def test_failure_result() -> None:
    result = Result.failure("Something went wrong.")

    assert not result.is_success
    assert result.value is None
    assert result.error == "Something went wrong."
    