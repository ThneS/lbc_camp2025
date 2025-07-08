# 登链社区 2025 训练营

# https://learnblockchain.cn/article/17585

## decert 与文件对应关系：

[POW](https://decert.me/quests/45779e03-7905-469e-822e-3ec3746d9ece) BaseDemo/pow.py
[GAS](https://decert.me/quests/d17a9270-99c3-4aeb-8a46-42ecb5e92792) BaseDemo/gas.py
[实践 POW 与非对称加密](https://decert.me/claim/45779e03-7905-469e-822e-3ec3746d9ece)：BaseDemo/rsa.py

[CHAIN](https://decert.me/quests/ed2d8324-54b0-4b7a-9cee-5e97d3c30030) Chain/main.py
[FirstContract](https://decert.me/quests/d17a9270-99c3-4aeb-8a46-42ecb5e92792) FirstContract

[模拟实现最小的区块链原理](https://decert.me/quests/ed2d8324-54b0-4b7a-9cee-5e97d3c30030)：MiniBlcokChain

[用 Solidity 编写 Bank 智能合约](https://decert.me/quests/c43324bc-0220-4e81-b533-668fa644c1c3)：BankSmartContract

[通过编写 BigBank 实践 Solidity 继承及接口合约交互](https://decert.me/quests/063c14be-d3e6-41e0-a243-54e35b1dde58)：BigBankSmartContract

[编写 ERC20 token 合约](https://decert.me/quests/aa45f136-27a3-4bc9-b4f7-15308e1e0daa)：ERC20Token

[Solidity 编写 TokenBank](https://decert.me/quests/eeb9f7d8-6fd0-4c38-b09c-75a29bd53af3)：TokenBank_V1

[扩展 ERC20 加入 Hook，并使用 Hook](https://decert.me/quests/4df553df-fbab-49c8-a05f-83256432c6af)：TokenBank_V2

[Solidity 实现用 Token 购买 NFT](https://decert.me/quests/abdbc346-8314-4394-8f97-8732780602ed)：NFTMarket_V1

[使用 Foundry 测试 Bank 合约](https://decert.me/quests/b8cde6b2-bad4-4629-b73a-2d0dede4f347)：Foundry/src/Bank_Contract.sol、Foundry/test/Bank.t.sol

[Foundry 高阶测试](https://decert.me/quests/08973815-3ebe-48d1-915e-7fc67c448763)：Foundry/src/NFT_Market.sol、Foundry/test/NFTMarket.t.sol

[使用 Viem 为 TokenBank 搭建一个简单的前端](https://decert.me/quests/56e455b3-901c-415d-90c0-a20759469cf9)：FrontEnd/viem-front/app/page.tsx

[使⽤ Viem.sh 监听 NFTMarket 的买卖记录](https://decert.me/quests/b4698649-25b2-45ae-9bb5-23da0c49e491)：FrontEnd/demo/src/watchTransfer.ts

[使用 Viem 构建一个 CLI 钱包](https://decert.me/quests/992dae0f-3bdf-4f03-9798-3427234fad95)：FrontEnd/demo/src/build_tx_keystore.ts

[实现一个简单的多签合约](https://decert.me/quests/f832d7a2-2806-4ad9-8560-a27ad8570c6f)：Foundry/src/ContractWallet.sol

[DApp 接入 AppKit 登录](https://decert.me/quests/a1a9aff6-1788-4254-bc47-405cc529bbd1)：FrontEnd/wagmi-front/app/page.tsx

[使用 EIP712 进行链下 Permit 和 白名单设计](https://decert.me/quests/fc66ef6c-35db-4ee7-b11d-c3b2d3fa356a)：Foundry/src/TokenBank_Permit.sol、Foundry/src/ERC20_Permit.sol、FrontEnd/viem-front/app/page_permit.tsx(测试时把这个文件名改成 page.tsx 即可)

[理解 Permit2 及实践](https://decert.me/quests/1fa3ecbc-a3cd-43ae-908e-661aac97bdc0)：Foundry/src/TokenBank_Permit2.sol

[使用 Viem 索引链上 ERC20 转账数据并展示](https://decert.me/quests/ae220513-c0cb-4d9b-873a-caee1d4b358e)：：FrontEnd/my-sqlite-app/watcher.js、FrontEnd/my-sqlite-app/index.js、FrontEnd/wagmi-front/app/page_transfer.tsx

[用最小代理实现 ERC20 铸币工厂](https://decert.me/quests/75782f22-edb8-4e82-9b68-0a4f46fcaadd)：Foundry/src/Meme_Factory.sol、Foundry/test/Meme_Factory.t.sol

[使用 Solidity 内联汇编修改合约 Owner 地址](https://decert.me/quests/163c68ab-8adf-4377-a1c2-b5d0132edc69)：Foundry/src/MyWallet.sol

[组合使用 MerkleTree 白名单、 Permit 授权 及 Multicall](https://decert.me/quests/faa435a5-f462-4f92-a209-3a7e8fdc4d81)：Foundry/src/AirdopMerkleNFTMarket.sol、Foundry/test/AirdopMerkleNFTMarket.t.sol

[编写一个可升级的 NFT Market 合约](https://decert.me/quests/ddbdd3c4-a633-49d7-adf9-34a6292ce3a8)：Foundry/src/ERC721_Upgrade.sol、Foundry/src/ERC721_Upgrade_V2.sol、Foundry/src/NFTMarketV1.sol、Foundry/src/NFTMarketV2.sol

[安全挑战：Hack Vault](https://decert.me/quests/b5368265-89b3-4058-8a57-a41bde625f5b)：Foundry/test/Vault.t.sol

[编写一个线性解锁（ Vesting） 合约](https://decert.me/quests/58aec80f-8980-434a-b549-566003367694)：Foundry/src/Vesting.sol、Foundry/test/Vesting.t.sol

[实现一个 LaunchPad 平台](https://decert.me/quests/df4886bc-65c6-45fb-ad0c-3389a9f99bf2)：Foundry/src/Meme_FactoryV2.sol、Foundry/test/MemeFactoryV2.t.sol

[获取 Uniswap v2 中 TWAP 价格](https://decert.me/quests/ff20bbfe-0345-4f32-8ca3-fa77b3a0d6cb)：Foundry/src/OracleSimple.sol、Foundry/test/OracleSimple.t.sol

[模拟闪电兑换套利](https://decert.me/quests/2a63cf95-43ec-42ee-975f-2b41510492cd)：Foundry/src/TokenA.sol、Foundry/src/TokenB.sol、Foundry/src/UniswapV2Factory.sol、Foundry/src/UniswapV2Router.sol、Foundry/src/FlashSwap.sol

[用 Solidity 编写 ETH 质押挖矿合约](https://decert.me/quests/e76599d5-a30c-4678-ba92-fe43c56df1db)：Foundry/src/StakingPool.sol

[实现一个 rebase 型 Token](https://decert.me/quests/2d4df0b6-17dc-4e5b-8f3a-728ed855e292)：Foundry/src/Rebase_Token.sol

[实现一个极简的杠杆 DEX](https://decert.me/quests/832502d6-e09a-4e08-9d0a-22b1ac51c1be)：Foundry/src/SimpleLeverageDEX.sol、Foundry/test/SimpleLeverageDEX.t.sol

[设计一个看涨期权 Token](https://decert.me/quests/5725236b-4e24-4c28-be69-2509087157c4)：Foundry/src/CallOptionToken.sol、Foundry/test/CallOptionToken.t.sol

[实现基于 Token 投票治理](https://decert.me/quests/4cbe2544-6848-4881-b2f5-c4f291241621)：Foundry/src/VoteToken.sol、Foundry/src/Gov.sol、Foundry/src/Bank.sol、Foundry/test/DAOTest.t.sol

[利用 FlashBots 捆绑交易](https://decert.me/quests/70957dea-e3de-4b45-82c2-5c105c56c4ae)：Foundry/src/flashbot_bundle.js

[EIP 7702 实践：发起打包交易](https://decert.me/quests/2c550f3e-0c29-46f8-a9ea-6258bb01b3ff)：Foundry/src/SimpleDelegateContract.sol、FrontEnd/viem-front/app/page_7702.tsx

[编写第一个 Solana 程序（Program）](https://decert.me/quests/90c331f2-6a0e-4a68-bc32-a50e1879a4bb)：SolanaProject/programs/my_solana_project/src/lib.rs

[编写脚本调用 Solana 链上程序](https://decert.me/quests/e2ea3b7a-07ac-4c35-8513-c25010b48d81)：SolanaProject/scripts/counter_script.ts
