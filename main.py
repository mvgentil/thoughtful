import pandas as pd
from sorter import sort


if __name__ == "__main__":

    print("Starting the package sorting process...")
    cleaned_lines = []
    with open("data/packages.csv", "r", encoding="utf-8") as f:
        for line in f:
            # Remove whitespace and newlines
            stripped = line.strip()
            # Skip empty lines
            if not stripped:
                continue
            # Count columns (split by comma)
            columns = [c for c in stripped.split(",")]
            if len(columns) == 4 or stripped.lower().startswith("width,height,length,mass"):
                cleaned_lines.append(line)

    with open("data/packages_cleaned.csv", "w", encoding="utf-8") as f:
        f.writelines(cleaned_lines)
    try:
        df = pd.read_csv("data/packages_cleaned.csv")
        df.columns = ["Width", "Height", "Length", "Mass"]

        # Convert all columns to float, invalid parsing will be set as NaN
        for col in ["Width", "Height", "Length", "Mass"]:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        # Drop rows with any NaN (i.e., non-float values)
        df = df.dropna(subset=["Width", "Height", "Length", "Mass"])
        df = df[(df["Width"] >= 0) & (df["Height"] >= 0) & (df["Length"] >= 0) & (df["Mass"] >= 0)]

        # Apply the sorting function to each row
        df["Stack"] = df.apply(lambda row: sort(row["Width"], row["Height"], row["Length"], row["Mass"]), axis=1)

        #df.to_csv("data/packages_sorted.csv", index=False)
        print("CSV file processed and sorted successfully.")

        # Percentage of packages in each stack
        stack_counts = df["Stack"].value_counts(normalize=True) * 100
        print("\nPercentage of packages in each stack:")
        for stack, percentage in stack_counts.items():
            print(f"{stack}: {percentage:.2f}% / {len(df[df['Stack'] == stack])} packages")

        # total number of packages
        total_packages = len(df)
        print(f"\nTotal number of packages: {total_packages}")

        #Average, minimum, and maximum Mass and Volume for each stack.
        df["Volume"] = df["Width"] * df["Height"] * df["Length"]
        stack_stats = df.groupby("Stack").agg({
            "Mass": ["mean", "min", "max"],
            "Volume": ["mean", "min", "max"]
        }).reset_index()
        print("\nAverage, minimum, and maximum Mass and Volume for each stack:")
        print(stack_stats)

        
    except Exception as e:
        print(f"Error reading CSV file: {e}")