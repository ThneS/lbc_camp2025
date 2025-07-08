print("""
实际支付费用 = gas_used × (base_fee_per_gas + priority_fee)
但在发起交易时，钱包必须保证：
    账户余额 ≥ gas_limit × max_fee_per_gas
所需余额 = 10,000 × 10 GWei = 100,000 GWei = 0.0001 ETH
用户的钱包余额至少要有 100,000 GWei（即 0.0001 ETH），才能成功提交该交易。

| 名称                         | 作用                                                      |
| -------------------------- | ------------------------------------------------------- |
| `gas_limit`                | 交易最多能消耗多少 gas                                           |
| `max_fee_per_gas`          | 用户愿意支付的最高 gas 单价                                        |
| `max_priority_fee_per_gas` | 给矿工的小费，影响打包优先级                                          |
| `base_fee_per_gas`         | 网络动态调整，交易执行时才知道                                         |
| `实际成本`                     | ≈ gas\_used × (base\_fee + priority\_fee)，通常 < max\_fee |

      """)