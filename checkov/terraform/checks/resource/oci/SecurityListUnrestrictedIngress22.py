from checkov.terraform.checks.resource.oci.AbsSecurityListUnrestrictedIngress import AbsSecurityListUnrestrictedIngress


class SecurityListUnrestrictedIngress22(AbsSecurityListUnrestrictedIngress):
    def __init__(self):
        super().__init__(check_id="CKV_OCI_19", port=22)


check = SecurityListUnrestrictedIngress22()
