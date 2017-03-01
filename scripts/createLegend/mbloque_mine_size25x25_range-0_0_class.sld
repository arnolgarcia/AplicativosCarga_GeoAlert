<?xml version="1.0" encoding="UTF-8"?>
<sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
  <sld:NamedLayer>
    <sld:Name>Mineralizacion</sld:Name>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>Mineralizacion</sld:Name>
      <sld:Title>Mineralizacion</sld:Title>
      <sld:Abstract>abstract</sld:Abstract>
      <sld:FeatureTypeStyle>
        <sld:Name>name</sld:Name>
        <sld:FeatureTypeName>Feature</sld:FeatureTypeName>
        <sld:SemanticTypeIdentifier>generic:geometry</sld:SemanticTypeIdentifier>
        <sld:SemanticTypeIdentifier>colorbrewer:quantile:personal</sld:SemanticTypeIdentifier>
		<sld:Rule>
          <sld:Name>Mixto</sld:Name>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>mine</ogc:PropertyName>
              <ogc:Literal>1</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#66c2a5</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
		<sld:Rule>
          <sld:Name>Mixto</sld:Name>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>mine</ogc:PropertyName>
              <ogc:Literal>4</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#fa8e63</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
		<sld:Rule>
          <sld:Name>Oxido</sld:Name>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>mine</ogc:PropertyName>
              <ogc:Literal>5</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#8da0cb</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
		<sld:Rule>
          <sld:Name>Primario + Bornita</sld:Name>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>mine</ogc:PropertyName>
              <ogc:Literal>6</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#e68ac3</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
		<sld:Rule>
          <sld:Name>Primario</sld:Name>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>mine</ogc:PropertyName>
              <ogc:Literal>7</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#a7d854</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
		<sld:Rule>
          <sld:Name>Esteril</sld:Name>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>mine</ogc:PropertyName>
              <ogc:Literal>8</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#ffd92f</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
		<sld:Rule>
          <sld:Name>Lixiviado</sld:Name>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>mine</ogc:PropertyName>
              <ogc:Literal>0</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#e4c494</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </sld:NamedLayer>
</sld:StyledLayerDescriptor>