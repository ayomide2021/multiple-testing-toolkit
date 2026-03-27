# all import 

def main():
    data = load_data("data/raw/data.csv")
    cleaned = clean_data(data)
    print("Pipeline ran successfully")

if __name__ == "__main__":
    main()
