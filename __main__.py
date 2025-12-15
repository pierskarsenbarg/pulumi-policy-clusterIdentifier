from pulumi_policy import (
    EnforcementLevel,
    PolicyPack,
    ReportViolation,
    ResourceValidationArgs,
    ResourceValidationPolicy,
)

def k8s_provider_cluster_identifier_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type == "pulumi:providers:kubernetes":
        if "clusterIdentifier" not in args.props or args.props["clusterIdentifier"] == "":
            report_violation("You should set the clusterIdentifier property so that the Kubernetes provider resources will not be replaced until this value is changed.", args.urn)

k8s_provider_cluster_identifier = ResourceValidationPolicy(
    name="k8s-provider-cluster-identifier",
    description="Ensures that the cllusterIdentifier property is set on the Kubernetes provider resource.",
    enforcement_level=EnforcementLevel.ADVISORY,
    validate=k8s_provider_cluster_identifier_validator,
)

PolicyPack(
    name="k8s-provider-policies",
    policies=[
        k8s_provider_cluster_identifier,
    ],
)
