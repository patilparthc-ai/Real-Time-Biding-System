#gives real time experience by takingg the pause for auction result
import time

# --- Define the ad slot --- in the form of dictionary
ad_slot = {
    "slot_id": "homepage_top_banner",
    "min_bid": 1.0  # Minimum bid allowed
}

# --- List of advertisers ---
advertisers = ["Nike", "Adidas", "Puma", "Reebok"]

# --- Function to get bids from user for each advertiser ---....list is used to stor the bid 
def get_user_bids():
    bids = []
    print(f"\n Ad Slot: {ad_slot['slot_id']} | Minimum Bid: ${ad_slot['min_bid']}")
    print(" Enter your bid (in USD) for each advertiser:")
# Here the for loop is appkied to get the different advertiser bids 
# Use of if satement to get the valid bid
    for adv in advertisers:
        while True:
            try:
                bid = float(input(f"{adv}'s Bid: $"))
                if bid < 0:
                    print(" Bid cannot be negative. Try again.")
                    continue
                bids.append((bid, adv))
                break
            except ValueError:
                print("Please enter a valid number.")
    return bids

# --- Function to run one auction round at a time ---
def run_auction(round_num):
    print(f"\n==============================")
    print(f" Auction Round {round_num}")
    print(f"==============================")

    bids = get_user_bids() #function is used to get the bid from the user stored in the ealier function 
    winner = max(bids, key=lambda x: x[0])

    if winner[0] >= ad_slot["min_bid"]:
        print(f"\n Winner: {winner[1]} with bid: ${winner[0]}")
    else:
        print("\n No valid bids. Ad slot remains unsold.")

# --- Run 3 auction rounds using the for loop ---
for round_num in range(1, 4):
    run_auction(round_num)
    time.sleep(1)  # Optional pause between rounds