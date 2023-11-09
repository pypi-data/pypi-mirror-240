import argparse
import subprocess

def configure_cron(schedule):
    # Generate the crontab entry
    cron_entry = f"{schedule} /path/to/your/script.py"
    
    # Add the entry to the user's crontab
    subprocess.run(["crontab", "-l", "|", "echo", "\"{}\"".format(cron_entry), "|", "crontab", "-"])

def main():
    parser = argparse.ArgumentParser(description="Configure cron schedule for your script.")
    parser.add_argument("--schedule", type=str, help="Cron schedule (e.g., '0 7 * * *' for 7:00 AM daily)")
    args = parser.parse_args()

    if args.schedule:
        configure_cron(args.schedule)
        print("Cron schedule configured successfully.")

if __name__ == "__main__":
    main()
