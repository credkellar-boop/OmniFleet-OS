import logging

class BillingEngine:
    def __init__(self):
        self.accounting_currency = "USD"
        self.infrastructure_fee_pct = 0.10

    def finalize_invoice(self, minutes_rented: int, rate_per_min: float, auxiliary_tolls: float) -> dict:
        """Compiles gross operational income and nets regional infrastructure processing fees."""
        gross_accrued = (minutes_rented * rate_per_min) + auxiliary_tolls
        net_revenue_share = gross_accrued * (1.0 - self.infrastructure_fee_pct)
        
        logging.info(f"Transaction finalized. Gross Yield: ${gross_accrued:.2f} | Net Fleet Revenue: ${net_revenue_share:.2f}")
        return {
            "gross_charge": round(gross_accrued, 2),
            "net_payout": round(net_revenue_share, 2),
            "billing_status": "SETTLED"
        }
      
