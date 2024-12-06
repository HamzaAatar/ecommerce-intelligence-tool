import click
from rich.console import Console
from rich.table import Table

from config import Config
from builtwith_extractor import BuiltWithExtractor
from amazon_validator import AmazonValidator
from email_extractor import EmailExtractor


@click.command()
@click.option("--output", default="ecommerce_analysis.csv", help="Output CSV filename")
@click.option(
    "--limit", default=None, type=int, help="Limit number of websites to analyze"
)
def main(output, limit):
    """E-commerce Website Intelligence Tool"""
    console = Console()
    Config.validate_config()

    with console.status("[bold green]Initializing analysis...") as _:
        try:
            # Extract websites
            websites_df = BuiltWithExtractor.extract_ecommerce_data(limit)

            if websites_df.empty:
                console.print("[bold red]No websites found for analysis")
                return

            # Validate Amazon presence
            websites = websites_df["Website"].tolist()
            amazon_presence = AmazonValidator.validate_amazon_presence(websites)
            websites_df["Listed on Amazon"] = websites_df["Website"].map(
                amazon_presence
            )

            # Extract emails
            email_data = EmailExtractor.extract_emails(websites)
            websites_df["Verified Email"] = websites_df["Website"].map(
                lambda x: email_data.get(x, {}).get("Verified Email", "No")
            )
            websites_df["Email"] = websites_df["Website"].map(
                lambda x: email_data.get(x, {}).get("Email", "")
            )

            # Export results
            websites_df.to_csv(output, index=False)

            # Display results summary
            table = Table(title="E-commerce Website Analysis")
            table.add_column("Website", style="cyan")
            table.add_column("Amazon Listed", style="magenta")
            table.add_column("Email Verified", style="green")

            for _, row in websites_df.iterrows():
                table.add_row(
                    row["Website"], row["Listed on Amazon"], row["Verified Email"]
                )

            console.print(table)
            console.print(
                f"[bold green]✅ Analysis complete. Results saved to {output}"
            )

        except Exception as e:
            console.print(f"[bold red]❌ Analysis failed: {e}")
            console.print_exception()


if __name__ == "__main__":
    main()
