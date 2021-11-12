#!/usr/bin/python3
import pandas
def main():
    df = pandas.read_excel("movies.xls")
    df.to_csv("movies.csv")
if __name__ == "__main__":
    main()
