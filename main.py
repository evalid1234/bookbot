from stats import word_count,char_count, sorted_dicts
import sys
 
def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text
def print_stats_formatted_string(sorted_list):
    formatted_string = ""
    for dictionary in sorted_list:
        formatted_string+=f"{dictionary['char']}: {dictionary['num']}\n"
    return formatted_string

def main(path):
    path = path
    text = get_book_text(path)
    num_words = word_count(text)
    char_count_dict = char_count(text)
    sorted_list = sorted_dicts(char_count_dict)
    formatted_string = print_stats_formatted_string(sorted_list)
    print(f"""
============ BOOKBOT ============\n
analyzing book found at {path}...\n
----------- Word Count ----------\n
Found {num_words} total words\n
--------- Character Count -------\n
{formatted_string}
============= END ===============
""")

if __name__ == "__main__":
    usage_message = """Usage: python3 main.py <path_to_book>\n"""
    if len(sys.argv) != 2:
        print(usage_message)
        sys.exit(1)
    path = sys.argv[1]
    try:
        main(path)
    except FileNotFoundError:
        print(f"File not found: {path}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

