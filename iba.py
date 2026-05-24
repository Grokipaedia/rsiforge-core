# governance/iba.py


class IBA:
    """
    Intent Bound Authorization (IBA)

    Purpose:
    - validate mutation intent
    - constrain unsafe runtime behavior
    - prevent uncontrolled self-modification

    IBA is the governance boundary
    between mutation proposal and execution.
    """

    def __init__(self):

        # Explicitly forbidden mutation actions
        self.forbidden_actions = [
            "rewrite_metric",
            "rewrite_iba",
            "rewrite_governance",
            "self_replicate",
            "expand_objectives",
            "disable_memory",
            "delete_memory",
            "rewrite_runtime",
            "external_network_access",
            "spawn_unbounded_processes"
        ]

        # Allowed runtime mutation types
        self.allowed_actions = [
            "maintain",
            "mutate_strategy"
        ]

    # -------------------------
    # Validate intent
    # -------------------------
    def validate_intent(self, proposal):
        """
        Validates mutation proposal before execution.

        Returns:
            True  -> allowed
            False -> blocked
        """

        action = proposal.get("action")

        # Block forbidden actions immediately
        if action in self.forbidden_actions:
            return False

        # Reject unknown actions
        if action not in self.allowed_actions:
            return False

        return True

    # -------------------------
    # Explain rejection
    # -------------------------
    def explain_rejection(self, proposal):
        """
        Provides human-readable rejection reason.
        """

        action = proposal.get("action")

        if action in self.forbidden_actions:
            return f"forbidden_action:{action}"

        if action not in self.allowed_actions:
            return f"unknown_action:{action}"

        return "approved"

    # -------------------------
    # Register new allowed action
    # -------------------------
    def register_allowed_action(self, action_name):
        """
        Adds safe mutation category.
        """

        if action_name not in self.allowed_actions:
            self.allowed_actions.append(action_name)

    # -------------------------
    # Governance status
    # -------------------------
    def status(self):
        """
        Returns governance state.
        """

        return {
            "allowed_actions": self.allowed_actions,
            "forbidden_actions": self.forbidden_actions
        }
