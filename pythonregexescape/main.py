import sys
import re

from pydantic import HttpUrl
from pydantic_core import Url

url_base = "https://mycompany/"

search_term = "John"

text = f"Here are the options that match your contact search criteria for the name \"{search_term}\":\n"\
" - Johnathan\n"\
" - John Farmer\n"\
" - John Johnson\n"\
" - John Citizen [XR]\n"\
""\
"Please pick a specific option from the given list."

links = {
    "Johnathan": Url(f"{url_base}/user/id=1"),
    "John Farmer": Url(f"{url_base}/user/id=2"),
    "John Johnson": Url(f"{url_base}/user/id=3"),
    "John Citizen [XR]": Url(f"{url_base}/user/id=4"),
}

def main(args: list[str] = sys.argv[1:]) -> None:
    noob_replace()
    regex_replace()
    simple_replace()


def noob_replace():
    open_bracket_placeholder = "PLACEHOLDER_OPEN_BRACKET"
    close_bracket_placeholder = "PLACEHOLDER_CLOSE_BRACKET"

    def _substitute_square_brackets(text: str, open_bracket: str, close_bracket: str) -> str:
        text = text.replace("[", open_bracket)
        text = text.replace("]", close_bracket)
        return text

    def _replace_text_with_link(match: re.Match) -> str:
        text = match.group(1)
        url = text_to_url_mapping.get(text)
        if url:
            return f"[{text}]({url})"
        return text  # Returns text if no URL is found

    def _compile_pattern_from_keys(keys: list[str]) -> re.Pattern:
        """Compile a regex pattern to match text keys, avoiding partial matches."""
        escaped_keys = [re.escape(key) for key in keys]
        pattern_str = r"(?<![\[\w\"'])\b(" + "|".join(escaped_keys) + r")\b(?![\w\"'])"
        return re.compile(pattern_str)

    def _create_text_to_url_mapping() -> dict[str, Url]:
        """Create a mapping of text to URLs, substituting brackets in the text."""
        mapping = {}
        for key, url in links.items():
                new_key = _substitute_square_brackets(key, open_bracket_placeholder, close_bracket_placeholder)
                mapping[new_key] = url
        return mapping

    # Prepare and process replacement content, apply placeholders for nested brackets
    replace_text = _substitute_square_brackets(
        text=text,
        open_bracket=open_bracket_placeholder,
        close_bracket=close_bracket_placeholder,
    )

    text_to_url_mapping = _create_text_to_url_mapping()

    # Sort keys by length (longest first) to avoid partial match issues
    sorted_keys = sorted(text_to_url_mapping.keys(), key=len, reverse=True)
    pattern = _compile_pattern_from_keys(sorted_keys)

    # Replace text with links, re-apply nested brackets
    replace_text = re.sub(pattern, _replace_text_with_link, replace_text)
    replace_text = replace_text.replace(open_bracket_placeholder, "[")
    replace_text = replace_text.replace(close_bracket_placeholder, "]")

    print("---noob_replace---")
    print(replace_text)


def regex_replace():
    def _replace_text_with_link(match: re.Match) -> str:
        text = match.group()
        return f"[{text}]({links[text]})" if links.get(text) else text

    replace_text = text
    # Sort keys by length (longest first) to avoid partial match issues
    escaped_keys = [re.escape(key) for key in sorted(links.keys(), key=len, reverse=True)]
    pattern = re.compile("|".join(escaped_keys))
    replace_text = re.sub(pattern, _replace_text_with_link, replace_text)
    print("---regex_replace---")
    print(replace_text)


def simple_replace():
    replace_text = text
    for key, url in links.items():
        replace_text = replace_text.replace(key, f"[{key}]({url})")
    print("---simple_replace---")
    print(replace_text)


if __name__ == "__main__":
    main()
