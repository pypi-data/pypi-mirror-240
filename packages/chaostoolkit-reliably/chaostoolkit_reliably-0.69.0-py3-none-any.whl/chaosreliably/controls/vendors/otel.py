import os
from typing import Optional

from chaoslib.types import Configuration, Experiment, Journal, Secrets

__all__ = ["OTELVendorHandler"]


class OTELVendorHandler:
    @staticmethod
    def is_on() -> bool:
        try:
            from opentelemetry import trace  # noqa: F401
        except ImportError:
            return False

        return os.getenv("OTEL_EXPORTER_OTLP_TRACES_HEADERS") is not None

    def started(
        self,
        experiment: Experiment,
        plan_id: Optional[str],
        execution_id: str,
        execution_url: str,
        configuration: Configuration,
        secrets: Secrets,
    ) -> None:
        from opentelemetry import trace

        current_span = trace.get_current_span()
        current_span.set_attribute(
            "reliably.experiment.name", experiment["title"]
        )
        current_span.set_attribute("reliably.execution.id", execution_id)
        current_span.set_attribute("reliably.execution.url", execution_url)
        current_span.set_attribute("reliably.plan.id", plan_id)

    def finished(
        self, journal: Journal, configuration: Configuration, secrets: Secrets
    ) -> None:
        from opentelemetry import trace

        current_span = trace.get_current_span()
        current_span.set_attribute(
            "reliably.execution.status", journal["status"]
        )
        current_span.set_attribute(
            "reliably.execution.deviated", str(journal["deviated"])
        )
