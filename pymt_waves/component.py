from __future__ import absolute_import

from pymt.framework.bmi_bridge import bmi_factory

from .bmi import Waves

Waves = bmi_factory(Waves)

del bmi_factory
