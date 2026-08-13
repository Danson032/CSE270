import pytest
import json
from build_sentences import (
    get_seven_letter_word,
    parse_json_from_file,
    choose_sentence_structure,
    get_pronoun,
    get_article,
    get_word,
    fix_agreement,
    build_sentence,
    structures
)


def test_get_seven_letter_word(mocker):
    mock_input = mocker.patch("builtins.input", return_value="computer")
    result = get_seven_letter_word()
    assert result == "COMPUTER"
    mock_input.assert_called_once_with(
        "Please enter a word with at least 7 letters: "
    )


def test_get_seven_letter_word_error(mocker):
    mocker.patch("builtins.input", return_value="hello")
    with pytest.raises(ValueError):
        get_seven_letter_word()


def test_parse_json_from_file(tmp_path):
    test_data = {"test": "data"}
    file_path = tmp_path / "test.json"

    with open(file_path, "w") as file:
        json.dump(test_data, file)

    result = parse_json_from_file(file_path)

    assert result == test_data


def test_choose_sentence_structure(mocker):
    mock_choice = mocker.patch(
        "random.choice",
        return_value=structures[0]
    )

    result = choose_sentence_structure()

    assert result == structures[0]
    mock_choice.assert_called_once_with(structures)


def test_get_pronoun(mocker):
    mock_choice = mocker.patch(
        "random.choice",
        return_value="he"
    )

    result = get_pronoun()

    assert result == "he"
    mock_choice.assert_called_once()


def test_get_article(mocker):
    mock_choice = mocker.patch(
        "random.choice",
        return_value="the"
    )

    result = get_article()

    assert result == "the"
    mock_choice.assert_called_once()


def test_get_word():
    speech_part = [
        "apple",
        "banana",
        "cat",
        "dog"
    ]

    assert get_word("A", speech_part) == "apple"
    assert get_word("B", speech_part) == "banana"
    assert get_word("C", speech_part) == "cat"
    assert get_word("D", speech_part) == "dog"


def test_fix_agreement():
    sentence = ["he", "quickly", "run"]
    fix_agreement(sentence)
    assert sentence == ["he", "quickly", "runs"]

    sentence = ["a", "quickly", "apple"]
    fix_agreement(sentence)
    assert sentence == ["an", "quickly", "apple"]

    sentence = ["the", "quickly", "smart", "dog", "run"]
    fix_agreement(sentence)
    assert sentence == ["the", "quickly", "smart", "dog", "runs"]


def test_build_sentence(mocker):
    mocker.patch(
        "build_sentences.get_article",
        return_value="the"
    )

    mocker.patch(
        "build_sentences.get_pronoun",
        return_value="he"
    )

    data = {
        "adjectives": [
            "big", "blue", "calm", "dark",
            "eager", "fast", "good", "happy"
        ],
        "nouns": [
            "apple", "ball", "cat", "dog",
            "egg", "fish", "goat", "house"
        ],
        "verbs": [
            "run", "build", "cook", "dance",
            "eat", "fight", "go", "help"
        ],
        "adverbs": [
            "quickly", "boldly", "calmly", "daily",
            "eagerly", "fast", "gently", "happily"
        ],
        "prepositions": [
            "above", "by", "near", "under",
            "with", "from", "over", "through"
        ]
    }

    result = build_sentence(
        "ABCDEFG",
        structures[1],
        data
    )

    assert isinstance(result, str)
    assert len(result) > 0