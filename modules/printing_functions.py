def printing(paper_size, *works_to_print_name):
    print(f"\nPrinting on paper size of {paper_size} the following works: ")
    for work_to_print_name in works_to_print_name:
        print(f"- {work_to_print_name}")
