import pytest
from parser.parser import parse_packet, PacketParseError


def test_parse_valid_packet():
    raw = {"packet_id": 1, "rpm": "3000", "pressure": 100, "flow_rate": 200}
    parsed = parse_packet(raw)
    assert parsed["rpm"] == 3000.0
    assert parsed["pressure"] == 100.0
    assert parsed["flow_rate"] == 200.0


def test_parse_missing_field_raises():
    raw = {"packet_id": 1, "rpm": 3000, "pressure": 100}
    with pytest.raises(PacketParseError):
        parse_packet(raw)


def test_parse_bad_type_raises():
    raw = {"packet_id": 1, "rpm": "not-a-number", "pressure": 100, "flow_rate": 200}
    with pytest.raises(PacketParseError):
        parse_packet(raw)


def test_parse_non_dict_raises():
    with pytest.raises(PacketParseError):
        parse_packet("not a dict")
