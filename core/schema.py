"""
CharacterForge Domain Core schema definitions.
"""

SCHEMA_VERSION = "1.0"

ENTITY_REQUIRED_FIELDS = {
    "entity_id",
    "identity",
    "state",
    "variants",
    "metadata",
}

IDENTITY_REQUIRED_FIELDS = {
    "identity_id",
    "name",
    "entity_type",
    "anchors",
    "identity_properties",
    "created_at",
    "version",
}

STATE_REQUIRED_FIELDS = {
    "state_id",
    "entity_id",
    "properties",
    "active_variant_id",
    "timestamp",
    "version",
}

VARIANT_REQUIRED_FIELDS = {
    "variant_id",
    "source_entity_id",
    "name",
    "changes",
    "preserves_identity",
    "version",
}

TRANSFORMATION_REQUIRED_FIELDS = {
    "transformation_id",
    "source_entity_id",
    "source_state_id",
    "target_state_id",
    "operations",
    "reversible",
    "preserves_identity",
    "version",
}

METADATA_REQUIRED_FIELDS = {
    "schema_version",
    "source",
    "provenance",
    "tags",
    "created_at",
}

ENTITY_SCHEMA_VERSION = SCHEMA_VERSION
