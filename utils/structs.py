from dataclasses import dataclass


@dataclass
class UserStruct:
    email: str = None
    sc_session_id: str = None
    aspx_auth: str = None
    customer_guid: str = None
    customer_profile_id: str = None
    customer_payment_profile_id: str = None
    payment_guid: str = None
    shipping_id: str = None
    billing_id: str = None
    saved_ccs: dict = None
    user_info_and_cart: dict = None
    shipping_billing_info: dict = None

    def to_dict(self) -> dict:
        return {
            "Email": self.email,
            "SC Session ID": self.sc_session_id,
            "ASPX Auth": self.aspx_auth,
            "Customer GUID": self.customer_guid,
            "Customer Profile ID": self.customer_profile_id,
            "Customer Payment Profile ID": self.customer_payment_profile_id,
            "Payment GUID": self.payment_guid,
            "Shipping ID": self.shipping_id,
            "Billing ID": self.billing_id,
            "Saved CCs": self.saved_ccs,
            "User Info & Cart": self.user_info_and_cart,
            "Shipping & Billing Info": self.shipping_billing_info
        }
