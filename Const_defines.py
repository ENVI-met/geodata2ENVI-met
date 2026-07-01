################################################################################
# This file defines constants which are used in other files of the project.    #
# Change the values here to update each relevant line of code to the new value #
################################################################################

C_NODATA_VALUE = -999.0

C_COLOR_SCALE_STEPS = 20
C_COLOR_SCALE_NAME = 'Spectral'

# Interpolation: 0 = Discrete, 1 = Interpolated, 2 = Exact
C_COLOR_SCALE_INTERPOLATION = 1

# Mode: 0 = EqualInterval, 1 = Continous, 2 = Quantile
C_COLOR_SCALE_MODE = 0

C_COLOR_SCALE_INVERT = True
C_COLOR_SCALE_USE_CUSTOM = False
C_COLOR_SCALE_CUSTOM_PATH = ''

# Sampling: 1 (Bilinear (2x2 kernel)) and 3 (Cubic B-Spline (4x4 kernel)) work well
C_SAMPLING_METHOD = 1

C_TERRAIN_ID = 2

# Cross-version Qt field-type constants for QgsField.
# QGIS 3 / PyQt5: QVariant.Type.X is available.
# QGIS 4 / PyQt6: QVariant.Type does not exist; QgsField expects QMetaType.Type.X.
try:
    from qgis.PyQt.QtCore import QVariant as _QVariant
    FIELD_TYPE_INT = _QVariant.Type.Int
    FIELD_TYPE_STRING = _QVariant.Type.String
except (AttributeError, ImportError):
    from qgis.PyQt.QtCore import QMetaType as _QMetaType
    FIELD_TYPE_INT = _QMetaType.Type.Int
    FIELD_TYPE_STRING = _QMetaType.Type.QString