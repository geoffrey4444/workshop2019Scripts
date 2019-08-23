# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

LoadPalette(paletteName='BlackBackground')

# create a new 'PVD Reader'
ahApvd = PVDReader(FileName='AhA.pvd')
ahApvd.PointArrays = ['DimlessRicciScalar', 'RicciScalar', 'SpinFunction', 'WeylB_NN', 'WeylE_NN']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1838, 1116]

# show data in view
ahApvdDisplay = Show(ahApvd, renderView1)

# trace defaults for the display properties.
ahApvdDisplay.Representation = 'Surface'
ahApvdDisplay.ColorArrayName = [None, '']
ahApvdDisplay.OSPRayScaleArray = 'DimlessRicciScalar'
ahApvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
ahApvdDisplay.SelectOrientationVectors = 'DimlessRicciScalar'
ahApvdDisplay.ScaleFactor = 0.19899970023590985
ahApvdDisplay.SelectScaleArray = 'DimlessRicciScalar'
ahApvdDisplay.GlyphType = 'Arrow'
ahApvdDisplay.GlyphTableIndexArray = 'DimlessRicciScalar'
ahApvdDisplay.GaussianRadius = 0.009949985011795493
ahApvdDisplay.SetScaleArray = ['POINTS', 'DimlessRicciScalar']
ahApvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
ahApvdDisplay.OpacityArray = ['POINTS', 'DimlessRicciScalar']
ahApvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
ahApvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
ahApvdDisplay.SelectionCellLabelFontFile = ''
ahApvdDisplay.SelectionPointLabelFontFile = ''
ahApvdDisplay.PolarAxes = 'PolarAxesRepresentation'
ahApvdDisplay.ScalarOpacityUnitDistance = 0.4800261182501882

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
ahApvdDisplay.OSPRayScaleFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
ahApvdDisplay.ScaleTransferFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
ahApvdDisplay.OpacityTransferFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
ahApvdDisplay.DataAxesGrid.XTitleFontFile = ''
ahApvdDisplay.DataAxesGrid.YTitleFontFile = ''
ahApvdDisplay.DataAxesGrid.ZTitleFontFile = ''
ahApvdDisplay.DataAxesGrid.XLabelFontFile = ''
ahApvdDisplay.DataAxesGrid.YLabelFontFile = ''
ahApvdDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
ahApvdDisplay.PolarAxes.PolarAxisTitleFontFile = ''
ahApvdDisplay.PolarAxes.PolarAxisLabelFontFile = ''
ahApvdDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
ahApvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'PVD Reader'
ahBpvd = PVDReader(FileName='AhB.pvd')
ahBpvd.PointArrays = ['DimlessRicciScalar', 'RicciScalar', 'SpinFunction', 'WeylB_NN', 'WeylE_NN']

# show data in view
ahBpvdDisplay = Show(ahBpvd, renderView1)

# trace defaults for the display properties.
ahBpvdDisplay.Representation = 'Surface'
ahBpvdDisplay.ColorArrayName = [None, '']
ahBpvdDisplay.OSPRayScaleArray = 'DimlessRicciScalar'
ahBpvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
ahBpvdDisplay.SelectOrientationVectors = 'DimlessRicciScalar'
ahBpvdDisplay.ScaleFactor = 0.1677561348053903
ahBpvdDisplay.SelectScaleArray = 'DimlessRicciScalar'
ahBpvdDisplay.GlyphType = 'Arrow'
ahBpvdDisplay.GlyphTableIndexArray = 'DimlessRicciScalar'
ahBpvdDisplay.GaussianRadius = 0.008387806740269515
ahBpvdDisplay.SetScaleArray = ['POINTS', 'DimlessRicciScalar']
ahBpvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
ahBpvdDisplay.OpacityArray = ['POINTS', 'DimlessRicciScalar']
ahBpvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
ahBpvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
ahBpvdDisplay.SelectionCellLabelFontFile = ''
ahBpvdDisplay.SelectionPointLabelFontFile = ''
ahBpvdDisplay.PolarAxes = 'PolarAxesRepresentation'
ahBpvdDisplay.ScalarOpacityUnitDistance = 0.40531180773940884

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
ahBpvdDisplay.OSPRayScaleFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
ahBpvdDisplay.ScaleTransferFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
ahBpvdDisplay.OpacityTransferFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
ahBpvdDisplay.DataAxesGrid.XTitleFontFile = ''
ahBpvdDisplay.DataAxesGrid.YTitleFontFile = ''
ahBpvdDisplay.DataAxesGrid.ZTitleFontFile = ''
ahBpvdDisplay.DataAxesGrid.XLabelFontFile = ''
ahBpvdDisplay.DataAxesGrid.YLabelFontFile = ''
ahBpvdDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
ahBpvdDisplay.PolarAxes.PolarAxisTitleFontFile = ''
ahBpvdDisplay.PolarAxes.PolarAxisLabelFontFile = ''
ahBpvdDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
ahBpvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

# set active source
SetActiveSource(ahApvd)

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=ahApvd)

# show data in view
extractSurface1Display = Show(extractSurface1, renderView1)

# trace defaults for the display properties.
extractSurface1Display.Representation = 'Surface'
extractSurface1Display.ColorArrayName = [None, '']
extractSurface1Display.OSPRayScaleArray = 'DimlessRicciScalar'
extractSurface1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface1Display.SelectOrientationVectors = 'DimlessRicciScalar'
extractSurface1Display.ScaleFactor = 0.19899970023590985
extractSurface1Display.SelectScaleArray = 'DimlessRicciScalar'
extractSurface1Display.GlyphType = 'Arrow'
extractSurface1Display.GlyphTableIndexArray = 'DimlessRicciScalar'
extractSurface1Display.GaussianRadius = 0.009949985011795493
extractSurface1Display.SetScaleArray = ['POINTS', 'DimlessRicciScalar']
extractSurface1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface1Display.OpacityArray = ['POINTS', 'DimlessRicciScalar']
extractSurface1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface1Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface1Display.SelectionCellLabelFontFile = ''
extractSurface1Display.SelectionPointLabelFontFile = ''
extractSurface1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractSurface1Display.OSPRayScaleFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface1Display.ScaleTransferFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface1Display.OpacityTransferFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
extractSurface1Display.DataAxesGrid.XTitleFontFile = ''
extractSurface1Display.DataAxesGrid.YTitleFontFile = ''
extractSurface1Display.DataAxesGrid.ZTitleFontFile = ''
extractSurface1Display.DataAxesGrid.XLabelFontFile = ''
extractSurface1Display.DataAxesGrid.YLabelFontFile = ''
extractSurface1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
extractSurface1Display.PolarAxes.PolarAxisTitleFontFile = ''
extractSurface1Display.PolarAxes.PolarAxisLabelFontFile = ''
extractSurface1Display.PolarAxes.LastRadialAxisTextFontFile = ''
extractSurface1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(ahApvd, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(Input=extractSurface1)

# show data in view
generateSurfaceNormals1Display = Show(generateSurfaceNormals1, renderView1)

# trace defaults for the display properties.
generateSurfaceNormals1Display.Representation = 'Surface'
generateSurfaceNormals1Display.ColorArrayName = [None, '']
generateSurfaceNormals1Display.OSPRayScaleArray = 'DimlessRicciScalar'
generateSurfaceNormals1Display.OSPRayScaleFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.SelectOrientationVectors = 'DimlessRicciScalar'
generateSurfaceNormals1Display.ScaleFactor = 0.19899970023590985
generateSurfaceNormals1Display.SelectScaleArray = 'DimlessRicciScalar'
generateSurfaceNormals1Display.GlyphType = 'Arrow'
generateSurfaceNormals1Display.GlyphTableIndexArray = 'DimlessRicciScalar'
generateSurfaceNormals1Display.GaussianRadius = 0.009949985011795493
generateSurfaceNormals1Display.SetScaleArray = ['POINTS', 'DimlessRicciScalar']
generateSurfaceNormals1Display.ScaleTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.OpacityArray = ['POINTS', 'DimlessRicciScalar']
generateSurfaceNormals1Display.OpacityTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals1Display.DataAxesGrid = 'GridAxesRepresentation'
generateSurfaceNormals1Display.SelectionCellLabelFontFile = ''
generateSurfaceNormals1Display.SelectionPointLabelFontFile = ''
generateSurfaceNormals1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
generateSurfaceNormals1Display.OSPRayScaleFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
generateSurfaceNormals1Display.ScaleTransferFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
generateSurfaceNormals1Display.OpacityTransferFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
generateSurfaceNormals1Display.DataAxesGrid.XTitleFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.YTitleFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.ZTitleFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.XLabelFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.YLabelFontFile = ''
generateSurfaceNormals1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
generateSurfaceNormals1Display.PolarAxes.PolarAxisTitleFontFile = ''
generateSurfaceNormals1Display.PolarAxes.PolarAxisLabelFontFile = ''
generateSurfaceNormals1Display.PolarAxes.LastRadialAxisTextFontFile = ''
generateSurfaceNormals1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(extractSurface1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(ahBpvd)

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(Input=ahBpvd)

# show data in view
extractSurface2Display = Show(extractSurface2, renderView1)

# trace defaults for the display properties.
extractSurface2Display.Representation = 'Surface'
extractSurface2Display.ColorArrayName = [None, '']
extractSurface2Display.OSPRayScaleArray = 'DimlessRicciScalar'
extractSurface2Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface2Display.SelectOrientationVectors = 'DimlessRicciScalar'
extractSurface2Display.ScaleFactor = 0.1677561348053903
extractSurface2Display.SelectScaleArray = 'DimlessRicciScalar'
extractSurface2Display.GlyphType = 'Arrow'
extractSurface2Display.GlyphTableIndexArray = 'DimlessRicciScalar'
extractSurface2Display.GaussianRadius = 0.008387806740269515
extractSurface2Display.SetScaleArray = ['POINTS', 'DimlessRicciScalar']
extractSurface2Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface2Display.OpacityArray = ['POINTS', 'DimlessRicciScalar']
extractSurface2Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface2Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface2Display.SelectionCellLabelFontFile = ''
extractSurface2Display.SelectionPointLabelFontFile = ''
extractSurface2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractSurface2Display.OSPRayScaleFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface2Display.ScaleTransferFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface2Display.OpacityTransferFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
extractSurface2Display.DataAxesGrid.XTitleFontFile = ''
extractSurface2Display.DataAxesGrid.YTitleFontFile = ''
extractSurface2Display.DataAxesGrid.ZTitleFontFile = ''
extractSurface2Display.DataAxesGrid.XLabelFontFile = ''
extractSurface2Display.DataAxesGrid.YLabelFontFile = ''
extractSurface2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
extractSurface2Display.PolarAxes.PolarAxisTitleFontFile = ''
extractSurface2Display.PolarAxes.PolarAxisLabelFontFile = ''
extractSurface2Display.PolarAxes.LastRadialAxisTextFontFile = ''
extractSurface2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(ahBpvd, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Generate Surface Normals'
generateSurfaceNormals2 = GenerateSurfaceNormals(Input=extractSurface2)

# show data in view
generateSurfaceNormals2Display = Show(generateSurfaceNormals2, renderView1)

# trace defaults for the display properties.
generateSurfaceNormals2Display.Representation = 'Surface'
generateSurfaceNormals2Display.ColorArrayName = [None, '']
generateSurfaceNormals2Display.OSPRayScaleArray = 'DimlessRicciScalar'
generateSurfaceNormals2Display.OSPRayScaleFunction = 'PiecewiseFunction'
generateSurfaceNormals2Display.SelectOrientationVectors = 'DimlessRicciScalar'
generateSurfaceNormals2Display.ScaleFactor = 0.1677561348053903
generateSurfaceNormals2Display.SelectScaleArray = 'DimlessRicciScalar'
generateSurfaceNormals2Display.GlyphType = 'Arrow'
generateSurfaceNormals2Display.GlyphTableIndexArray = 'DimlessRicciScalar'
generateSurfaceNormals2Display.GaussianRadius = 0.008387806740269515
generateSurfaceNormals2Display.SetScaleArray = ['POINTS', 'DimlessRicciScalar']
generateSurfaceNormals2Display.ScaleTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals2Display.OpacityArray = ['POINTS', 'DimlessRicciScalar']
generateSurfaceNormals2Display.OpacityTransferFunction = 'PiecewiseFunction'
generateSurfaceNormals2Display.DataAxesGrid = 'GridAxesRepresentation'
generateSurfaceNormals2Display.SelectionCellLabelFontFile = ''
generateSurfaceNormals2Display.SelectionPointLabelFontFile = ''
generateSurfaceNormals2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
generateSurfaceNormals2Display.OSPRayScaleFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
generateSurfaceNormals2Display.ScaleTransferFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
generateSurfaceNormals2Display.OpacityTransferFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
generateSurfaceNormals2Display.DataAxesGrid.XTitleFontFile = ''
generateSurfaceNormals2Display.DataAxesGrid.YTitleFontFile = ''
generateSurfaceNormals2Display.DataAxesGrid.ZTitleFontFile = ''
generateSurfaceNormals2Display.DataAxesGrid.XLabelFontFile = ''
generateSurfaceNormals2Display.DataAxesGrid.YLabelFontFile = ''
generateSurfaceNormals2Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
generateSurfaceNormals2Display.PolarAxes.PolarAxisTitleFontFile = ''
generateSurfaceNormals2Display.PolarAxes.PolarAxisLabelFontFile = ''
generateSurfaceNormals2Display.PolarAxes.LastRadialAxisTextFontFile = ''
generateSurfaceNormals2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(extractSurface2, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(ahApvd)

# create a new 'Annotate Time Filter'
annotateTimeFilter1 = AnnotateTimeFilter(Input=ahApvd)

# show data in view
annotateTimeFilter1Display = Show(annotateTimeFilter1, renderView1)

# trace defaults for the display properties.
annotateTimeFilter1Display.FontFile = ''

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(ahApvd)

# set active source
SetActiveSource(generateSurfaceNormals1)

# set scalar coloring
ColorBy(generateSurfaceNormals1Display, ('POINTS', 'DimlessRicciScalar'))

# rescale color and/or opacity maps used to include current data range
generateSurfaceNormals1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
generateSurfaceNormals1Display.SetScalarBarVisibility(renderView1, False)

# get color transfer function/color map for 'DimlessRicciScalar'
dimlessRicciScalarLUT = GetColorTransferFunction('DimlessRicciScalar')

# get opacity transfer function/opacity map for 'DimlessRicciScalar'
dimlessRicciScalarPWF = GetOpacityTransferFunction('DimlessRicciScalar')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
dimlessRicciScalarLUT.ApplyPreset('Viridis (matplotlib)', True)

# Rescale transfer function
dimlessRicciScalarLUT.RescaleTransferFunction(0.48, 0.52)

# Rescale transfer function
dimlessRicciScalarPWF.RescaleTransferFunction(0.48, 0.52)

# set active source
SetActiveSource(generateSurfaceNormals2)

# set scalar coloring
ColorBy(generateSurfaceNormals2Display, ('POINTS', 'DimlessRicciScalar'))

# rescale color and/or opacity maps used to include current data range
generateSurfaceNormals2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
generateSurfaceNormals2Display.SetScalarBarVisibility(renderView1, False)

# set active source
SetActiveSource(annotateTimeFilter1)

# Properties modified on annotateTimeFilter1Display
annotateTimeFilter1Display.FontSize = 17

# Properties modified on annotateTimeFilter1Display
annotateTimeFilter1Display.FontSize = 16

# Properties modified on annotateTimeFilter1Display
annotateTimeFilter1Display.FontSize = 15

# Properties modified on annotateTimeFilter1Display
annotateTimeFilter1Display.FontSize = 14

# Properties modified on annotateTimeFilter1Display
annotateTimeFilter1Display.FontFamily = 'Times'

## create a new 'PVD Reader'
#ahCpvd = PVDReader(FileName='AhC.pvd')
#ahCpvd.PointArrays = ['DimlessRicciScalar', 'RicciScalar', 'SpinFunction', 'WeylB_NN', 'WeylE_NN']
#
## show data in view
#ahCpvdDisplay = Show(ahCpvd, renderView1)
#
## trace defaults for the display properties.
#ahCpvdDisplay.Representation = 'Surface'
#ahCpvdDisplay.ColorArrayName = [None, '']
#ahCpvdDisplay.OSPRayScaleArray = 'DimlessRicciScalar'
#ahCpvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
#ahCpvdDisplay.SelectOrientationVectors = 'DimlessRicciScalar'
#ahCpvdDisplay.ScaleFactor = 0.530855021129138
#ahCpvdDisplay.SelectScaleArray = 'DimlessRicciScalar'
#ahCpvdDisplay.GlyphType = 'Arrow'
#ahCpvdDisplay.GlyphTableIndexArray = 'DimlessRicciScalar'
#ahCpvdDisplay.GaussianRadius = 0.026542751056456898
#ahCpvdDisplay.SetScaleArray = ['POINTS', 'DimlessRicciScalar']
#ahCpvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
#ahCpvdDisplay.OpacityArray = ['POINTS', 'DimlessRicciScalar']
#ahCpvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
#ahCpvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
#ahCpvdDisplay.SelectionCellLabelFontFile = ''
#ahCpvdDisplay.SelectionPointLabelFontFile = ''
#ahCpvdDisplay.PolarAxes = 'PolarAxesRepresentation'
#ahCpvdDisplay.ScalarOpacityUnitDistance = 0.43568287455093985
#
## init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
#ahCpvdDisplay.OSPRayScaleFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]
#
## init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
#ahCpvdDisplay.ScaleTransferFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]
#
## init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
#ahCpvdDisplay.OpacityTransferFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]
#
## init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
#ahCpvdDisplay.DataAxesGrid.XTitleFontFile = ''
#ahCpvdDisplay.DataAxesGrid.YTitleFontFile = ''
#ahCpvdDisplay.DataAxesGrid.ZTitleFontFile = ''
#ahCpvdDisplay.DataAxesGrid.XLabelFontFile = ''
#ahCpvdDisplay.DataAxesGrid.YLabelFontFile = ''
#ahCpvdDisplay.DataAxesGrid.ZLabelFontFile = ''
#
## init the 'PolarAxesRepresentation' selected for 'PolarAxes'
#ahCpvdDisplay.PolarAxes.PolarAxisTitleFontFile = ''
#ahCpvdDisplay.PolarAxes.PolarAxisLabelFontFile = ''
#ahCpvdDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
#ahCpvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
#
## set active source
#SetActiveSource(ahCpvd)
#
## create a new 'Extract Surface'
#extractSurface3 = ExtractSurface(Input=ahCpvd)
#
## show data in view
#extractSurface3Display = Show(extractSurface3, renderView1)
#
## trace defaults for the display properties.
#extractSurface3Display.Representation = 'Surface'
#extractSurface3Display.ColorArrayName = [None, '']
#extractSurface3Display.OSPRayScaleArray = 'DimlessRicciScalar'
#extractSurface3Display.OSPRayScaleFunction = 'PiecewiseFunction'
#extractSurface3Display.SelectOrientationVectors = 'DimlessRicciScalar'
#extractSurface3Display.ScaleFactor = 0.530855021129138
#extractSurface3Display.SelectScaleArray = 'DimlessRicciScalar'
#extractSurface3Display.GlyphType = 'Arrow'
#extractSurface3Display.GlyphTableIndexArray = 'DimlessRicciScalar'
#extractSurface3Display.GaussianRadius = 0.026542751056456898
#extractSurface3Display.SetScaleArray = ['POINTS', 'DimlessRicciScalar']
#extractSurface3Display.ScaleTransferFunction = 'PiecewiseFunction'
#extractSurface3Display.OpacityArray = ['POINTS', 'DimlessRicciScalar']
#extractSurface3Display.OpacityTransferFunction = 'PiecewiseFunction'
#extractSurface3Display.DataAxesGrid = 'GridAxesRepresentation'
#extractSurface3Display.SelectionCellLabelFontFile = ''
#extractSurface3Display.SelectionPointLabelFontFile = ''
#extractSurface3Display.PolarAxes = 'PolarAxesRepresentation'
#
## init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
#extractSurface3Display.OSPRayScaleFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]
#
## init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
#extractSurface3Display.ScaleTransferFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]
#
## init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
#extractSurface3Display.OpacityTransferFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]
#
## init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
#extractSurface3Display.DataAxesGrid.XTitleFontFile = ''
#extractSurface3Display.DataAxesGrid.YTitleFontFile = ''
#extractSurface3Display.DataAxesGrid.ZTitleFontFile = ''
#extractSurface3Display.DataAxesGrid.XLabelFontFile = ''
#extractSurface3Display.DataAxesGrid.YLabelFontFile = ''
#extractSurface3Display.DataAxesGrid.ZLabelFontFile = ''
#
## init the 'PolarAxesRepresentation' selected for 'PolarAxes'
#extractSurface3Display.PolarAxes.PolarAxisTitleFontFile = ''
#extractSurface3Display.PolarAxes.PolarAxisLabelFontFile = ''
#extractSurface3Display.PolarAxes.LastRadialAxisTextFontFile = ''
#extractSurface3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
#
## hide data in view
#Hide(ahCpvd, renderView1)
#
## update the view to ensure updated data information
#renderView1.Update()
#
## create a new 'Generate Surface Normals'
#generateSurfaceNormals3 = GenerateSurfaceNormals(Input=extractSurface3)
#
## show data in view
#generateSurfaceNormals3Display = Show(generateSurfaceNormals3, renderView1)
#
## trace defaults for the display properties.
#generateSurfaceNormals3Display.Representation = 'Surface'
#generateSurfaceNormals3Display.ColorArrayName = [None, '']
#generateSurfaceNormals3Display.OSPRayScaleArray = 'DimlessRicciScalar'
#generateSurfaceNormals3Display.OSPRayScaleFunction = 'PiecewiseFunction'
#generateSurfaceNormals3Display.SelectOrientationVectors = 'DimlessRicciScalar'
#generateSurfaceNormals3Display.ScaleFactor = 0.530855021129138
#generateSurfaceNormals3Display.SelectScaleArray = 'DimlessRicciScalar'
#generateSurfaceNormals3Display.GlyphType = 'Arrow'
#generateSurfaceNormals3Display.GlyphTableIndexArray = 'DimlessRicciScalar'
#generateSurfaceNormals3Display.GaussianRadius = 0.026542751056456898
#generateSurfaceNormals3Display.SetScaleArray = ['POINTS', 'DimlessRicciScalar']
#generateSurfaceNormals3Display.ScaleTransferFunction = 'PiecewiseFunction'
#generateSurfaceNormals3Display.OpacityArray = ['POINTS', 'DimlessRicciScalar']
#generateSurfaceNormals3Display.OpacityTransferFunction = 'PiecewiseFunction'
#generateSurfaceNormals3Display.DataAxesGrid = 'GridAxesRepresentation'
#generateSurfaceNormals3Display.SelectionCellLabelFontFile = ''
#generateSurfaceNormals3Display.SelectionPointLabelFontFile = ''
#generateSurfaceNormals3Display.PolarAxes = 'PolarAxesRepresentation'
#
## init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
#generateSurfaceNormals3Display.OSPRayScaleFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]
#
## init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
#generateSurfaceNormals3Display.ScaleTransferFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]
#
## init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
#generateSurfaceNormals3Display.OpacityTransferFunction.Points = [6179.999999999999, 0.0, 0.5, 0.0, 398809631686991.2, 1.0, 0.5, 0.0]
#
## init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
#generateSurfaceNormals3Display.DataAxesGrid.XTitleFontFile = ''
#generateSurfaceNormals3Display.DataAxesGrid.YTitleFontFile = ''
#generateSurfaceNormals3Display.DataAxesGrid.ZTitleFontFile = ''
#generateSurfaceNormals3Display.DataAxesGrid.XLabelFontFile = ''
#generateSurfaceNormals3Display.DataAxesGrid.YLabelFontFile = ''
#generateSurfaceNormals3Display.DataAxesGrid.ZLabelFontFile = ''
#
## init the 'PolarAxesRepresentation' selected for 'PolarAxes'
#generateSurfaceNormals3Display.PolarAxes.PolarAxisTitleFontFile = ''
#generateSurfaceNormals3Display.PolarAxes.PolarAxisLabelFontFile = ''
#generateSurfaceNormals3Display.PolarAxes.LastRadialAxisTextFontFile = ''
#generateSurfaceNormals3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
#
## hide data in view
#Hide(extractSurface3, renderView1)
#
## update the view to ensure updated data information
#renderView1.Update()
#
## set active source
#SetActiveSource(generateSurfaceNormals3)
#
## set scalar coloring
#ColorBy(generateSurfaceNormals3Display, ('POINTS', 'DimlessRicciScalar'))
#
## rescale color and/or opacity maps used to include current data range
#generateSurfaceNormals3Display.RescaleTransferFunctionToDataRange(True, False)
#
## show color bar/color legend
#generateSurfaceNormals3Display.SetScalarBarVisibility(renderView1, False)
#
## get color legend/bar for dimlessRicciScalarLUT in view renderView1
#dimlessRicciScalarLUTColorBar = GetScalarBar(dimlessRicciScalarLUT, renderView1)
#
## set active source
#SetActiveSource(generateSurfaceNormals3)
#
## create a new 'Annotate Time Filter'
#annotateTimeFilter2 = AnnotateTimeFilter(Input=generateSurfaceNormals3)
#
## show data in view
#annotateTimeFilter2Display = Show(annotateTimeFilter2, renderView1)
#
## trace defaults for the display properties.
#annotateTimeFilter2Display.FontFile = ''
#
## update the view to ensure updated data information
#renderView1.Update()
#
## Properties modified on annotateTimeFilter2Display
#annotateTimeFilter2Display.FontSize = 17
#
## Properties modified on annotateTimeFilter2Display
#annotateTimeFilter2Display.FontSize = 16
#
## Properties modified on annotateTimeFilter2Display
#annotateTimeFilter2Display.FontSize = 15
#
## Properties modified on annotateTimeFilter2Display
#annotateTimeFilter2Display.FontSize = 14
#
## Properties modified on annotateTimeFilter2Display
#annotateTimeFilter2Display.FontFamily = 'Times'
#
## hide data in view
#Hide(annotateTimeFilter2, renderView1)
#
## hide data in view
#Hide(generateSurfaceNormals3, renderView1)
# set active source
#SetActiveSource(generateSurfaceNormals3)
#
## show data in view
#generateSurfaceNormals3Display = Show(generateSurfaceNormals3, renderView1)
#
## show color bar/color legend
#generateSurfaceNormals3Display.SetScalarBarVisibility(renderView1, False)

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
generateSurfaceNormals1Display.SetScalarBarVisibility(renderView1, False)

# get color legend/bar for dimlessRicciScalarLUT in view renderView1
dimlessRicciScalarLUTColorBar = GetScalarBar(dimlessRicciScalarLUT, renderView1)

# change scalar bar placement
dimlessRicciScalarLUTColorBar.Orientation = 'Horizontal'
dimlessRicciScalarLUTColorBar.WindowLocation = 'AnyLocation'
dimlessRicciScalarLUTColorBar.Position = [0.6449047878128401, 0.025089605734767012]
dimlessRicciScalarLUTColorBar.ScalarBarLength = 0.3300000000000002

dimlessRicciScalarLUT.RescaleTransferFunction(0.48, 0.52)
#
## Rescale transfer function
dimlessRicciScalarPWF.RescaleTransferFunction(0.48, 0.52)
generateSurfaceNormals1Display.SetScalarBarVisibility(renderView1, False)

# current camera placement for renderView1
renderView1.CameraPosition = [-42.49895285266955, -10.5378858318972, 10.673557845860767]
renderView1.CameraFocalPoint = [24.523697004336398, 6.6726273703796775, -6.758535428551902]
renderView1.CameraViewUp = [0.1727497823187046, 0.2828802707852527, 0.9434703308050032]
renderView1.CameraParallelScale = 18.469083388476736

# save animation
SaveAnimation('./PlungeFrame.png', renderView1, ImageResolution=[1920, 1080])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-42.49895285266955, -10.5378858318972, 10.673557845860767]
renderView1.CameraFocalPoint = [24.523697004336398, 6.6726273703796775, -6.758535428551902]
renderView1.CameraViewUp = [0.1727497823187046, 0.2828802707852527, 0.9434703308050032]
renderView1.CameraParallelScale = 18.469083388476736

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
