import argparse
import urllib.request
import urllib.parse
import json


# num of releases per page
PER_PAGE = 50


def show_releases(sdk: str) -> None:
    """
    Get sdk product, sdk version;
    use Github API to retrieve release
    info for given SDK.
    """
    params = urllib.parse.urlencode({"per_page": PER_PAGE})
    urls = {
        "web": f"https://api.github.com/repos/onfido/onfido-sdk-ui/releases?{params}",
        "android": f"https://api.github.com/repos/onfido/onfido-android-sdk/releases?{params}",
    }
    url = urls[sdk]
    request = urllib.request.Request(
        url=url, method="GET", headers={"accept": "application/vnd.github.v3+json"}
    )
    with urllib.request.urlopen(request) as response:
        releases = json.loads(response.read().decode("utf-8"))
        for res in releases:
            name = res.get("name", "Not found")
            body = res.get("body", "Not found")
            print("-" * 20)
            print(f"Release: {name}")
            print(body)


def get_options() -> argparse.Namespace:
    """
    Parse program arguments (from command line);
    return 'Namespace' object.
    """
    parser = argparse.ArgumentParser(
        prog="release parser",
        description="Parse release notes",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store",
        help="Select specific version",
        metavar="",
    )
    parser.add_argument(
        "-sdk", action="store", help="Select SDK Product", metavar="", default="web"
    )
    options = parser.parse_args()
    return options


if __name__ == "__main__":
    options = get_options()
    show_releases(options.sdk)
