# ShorterPy
A Python SDK for Shorter

## Installation

From PyPi

```
pip install shorter-py
```

## Documentation

Complete documentation coming soon

## Example Usage

The following examples shows how to use this packages in different use cases

### Create an APIProvider

```
from shorterpy.api.apiProvider import ApiProvider, Network
from eth_account import Account

acc = Account.from_key(<PRIVATE_KEY_HERE>)
api = ApiProvider(
        <RINKEBY_RPC_URL>, 
        Network.RINKEBY,
        acc
    )

```

### Provider Usecase

#### Create a Pool Proposal

Creating a pool proposal requires you to call `createPoolProposal` function in `Committee` contract. This function requires you to pay 10000 IPISTR tokens.
First, approve `Committee` to use 10000 IPISTR from your account:

```
from shorterpy.contracts.erc20 import ERC20
from shorterpy.common.types import GasParams

#Create IPISTR Token contract object
ipistr = ERC20(api, Web3.toChecksumAddress('0x7b113F4e8b55f812eC52B83313f6354364204DB2'))

#Create GasParams object, containing details about gas to be uses
gas_params = GasParams(gas=1000000, max_fee_per_gas=Web3.toWei(2, 'gwei'), max_priority_fee_per_gas=Web3.toWei(2, 'gwei'))

#Send a transaction to approve Committee contract to use 10000 IPISTRs, the transaction will be signed automatically by the ApiProvider
tx_receipt = ipistr.approve(ADDRESSES[Network.RINKEBY.name]['ICommittee'], 10000*(10**18), gas_params)

```

Then, send a transaction to create pool proposal

```
from shorterpy.contracts.committee import Committee

#Create Committee contract object
committee = Committee(api)

#Create GasParams object, containing details about gas to be uses
gas_params = GasParams(gas=1000000, max_fee_per_gas=Web3.toWei(2, 'gwei'), max_priority_fee_per_gas=Web3.toWei(2, 'gwei'))

#Send a transaction to create pool proposal function: Committee.createPoolProposal(staked_token, leverage, duration_days, gas_params)
tx_receipt = committee.createPoolProposal(<STAKED_TOKEN_ADDRESS>, 5, 30, gas_params)
```

#### Deposit And Withdraw

Providers can deposit into a pool and withdraw from it, using the StrPool contract object.

A StrPool contract object can be created with the following syntax:

```
from shorterpy.contracts.strPool import StrPool

strPool = StrPool(api, <POOL_ADDRESS>)
```

The pool address paramater is required to connect it to the required StrPool

The deposit and withdrawal is made through the token related with the pool. So, it is necessary to approve the pool to use
the required amount of tokens to make a deposit. 

```
from shorterpy.contracts.erc20 import ERC20
from shorterpy.common.types import GasParams

#Create Token contract object
token = ERC20(api, Web3.toChecksumAddress(<TOKEN_ADDRESS>))

#Create GasParams object, containing details about gas to be uses
gas_params = GasParams(gas=1000000, max_fee_per_gas=Web3.toWei(2, 'gwei'), max_priority_fee_per_gas=Web3.toWei(2, 'gwei'))

#Send a transaction to approve Committee contract to use 10000 IPISTRs, the transaction will be signed automatically by the ApiProvider
tx_receipt = token.approve(<POOL_ADDRESS>, <AMOUNT_TO_DEPOSIT>, gas_params)
```

Then, the deposit can be made by calling `strPool.deposit()` function

```
#Create GasParams object, containing details about gas to be uses
gas_params = GasParams(gas=1000000, max_fee_per_gas=Web3.toWei(2, 'gwei'), max_priority_fee_per_gas=Web3.toWei(2, 'gwei'))

tx_receipt = strPool.deposit(<AMOUNT_TO_DEPOSIT>, gas_params)
```

Withdrawal can be made by calling `strPool.withdraw()` function

```
tx_receipt = strPool.withdraw(<PERCENTAGE_TO_WITHDRAW>, <AMOUNT_TO_WITDRAW>, gas_params)
```

### Trader Usecase

Traders can use the `TradingHub` contract to buy cover or sell short

#### Sell Short

```
from shorterpy.contracts.tradingHub import TradingHub

tradingHub = TradingHub(api)

gas_params = GasParams(gas=1000000, max_fee_per_gas=Web3.toWei(2, 'gwei'), max_priority_fee_per_gas=Web3.toWei(2, 'gwei'))

tx_receipt = tradingHub.sell_short(<POOL_ID>, <AMOUNT>, <AMOUNT_OUT_MIN>, <SWAP_ROUTER>, <PATH>, gas_params)
```

#### Buy Cover

```
tx_receipt = tradingHub.buy_cover(<POOL_ID>, <AMOUNT>, <AMOUNT_IN_MAX>, <SWAP_ROUTER>, <PATH>, gas_params)
```


### Ruler Usecase

Rulers can participate in committee activities by deposits/withdrawal of IPISTR tokens in `Committee` contract. 

```
from shorterpy.contracts.committee import Committee

committee = Committee(api)

gas_params = GasParams(gas=1000000, max_fee_per_gas=Web3.toWei(2, 'gwei'), max_priority_fee_per_gas=Web3.toWei(2, 'gwei'))

#Deposit IPISTR to committee
tx_receipt = committee.deposit(amount, gas_params)

#Withdraw IPISTR from committee
tx_receipt = committee.withdraw(amount, gas_params)
```

Rulers can also vote on proposals

```
tx_receipt = committee.vote(<PROPOSAL_ID>, <DIRECTION - True/False>, <VOTE_SHARE>, gas_params)
```

Rulers can also participate in Tanto and Katana bids

```
from shorterpy.contracts.auctionHall import AuctionHall

auctionHall = AuctionHall(api)

gas_params = GasParams(gas=1000000, max_fee_per_gas=Web3.toWei(2, 'gwei'), max_priority_fee_per_gas=Web3.toWei(2, 'gwei'))

#Bid Tanto
tx_receipt = auctionHall.bid_tanto(<POSITION_ADDR>, <BID_SIZE>, <PRIORITY_FEE>, gas_params)

#Get phase1 infos
p1_info = auctionHall.phase1_infos(<POSITION_ADDR>)

#Bid Katana
tx_receipt = auctionHall.bid_katana(<POSITION_ADDR>, <PATH>, gas_params)

#get phase2 infos
p2_info = auctionHall.phase2_infos(<POSITION_ADDR>)
```

Rulers can also execute naginata

```
from shorterpy.contracts.vaultButler import VaultButler

vaultButler = VaultButler(api)

gas_params = GasParams(gas=1000000, max_fee_per_gas=Web3.toWei(2, 'gwei'), max_priority_fee_per_gas=Web3.toWei(2, 'gwei'))

#Execute Naginate
tx_receipt = vaultButler.execute_naginata(<POSITION_ADDR>, <BID_SIZE>, gas_params)
```

### Guest

Anyone can stake/unstake tokens from `Farming` contract for their participation in the platform.

```
from shorterpy.contracts.farming import Farming

farming = Farming(api)

gas_params = GasParams(gas=1000000, max_fee_per_gas=Web3.toWei(2, 'gwei'), max_priority_fee_per_gas=Web3.toWei(2, 'gwei'))

#Stake
tx_receipt = farming.stake(amount, gas_params)

#Unstake
tx_receipt = farming.unstake(amount, gas_params)
```

They can also harvest their rewards

```
#view pending rewards
rewards = farming.all_pending_rewards(<USER_ADDR>)

#haverst all rewards
tx_receipt = farming.harvest_all(
        <GOV_REWARDS>,
        <FARMING_REWARDS>,
        <VOTE_AGAINS_REWARDS>,
        <TRADING_REWARD_POOLS>,
        <STAKES_REWARD_POOLS>,
        <CREATE_REWARD_POOLS>,
        <VOTE_REWARD_POOLS>,
        gas_params
)
```
