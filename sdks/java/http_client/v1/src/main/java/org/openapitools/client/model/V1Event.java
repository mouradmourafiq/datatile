// Copyright 2018-2020 Polyaxon, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/*
 * Polyaxon SDKs and REST API specification.
 * Polyaxon SDKs and REST API specification.
 *
 * The version of the OpenAPI document: 1.1.8
 * Contact: contact@polyaxon.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import org.openapitools.client.model.V1EventArtifact;
import org.openapitools.client.model.V1EventAudio;
import org.openapitools.client.model.V1EventChart;
import org.openapitools.client.model.V1EventCurve;
import org.openapitools.client.model.V1EventDataframe;
import org.openapitools.client.model.V1EventHistogram;
import org.openapitools.client.model.V1EventImage;
import org.openapitools.client.model.V1EventModel;
import org.openapitools.client.model.V1EventVideo;
import org.threeten.bp.OffsetDateTime;

/**
 * V1Event
 */

public class V1Event {
  public static final String SERIALIZED_NAME_TIMESTAMP = "timestamp";
  @SerializedName(SERIALIZED_NAME_TIMESTAMP)
  private OffsetDateTime timestamp;

  public static final String SERIALIZED_NAME_STEP = "step";
  @SerializedName(SERIALIZED_NAME_STEP)
  private Integer step;

  public static final String SERIALIZED_NAME_METRIC = "metric";
  @SerializedName(SERIALIZED_NAME_METRIC)
  private Float metric;

  public static final String SERIALIZED_NAME_IMAGE = "image";
  @SerializedName(SERIALIZED_NAME_IMAGE)
  private V1EventImage image;

  public static final String SERIALIZED_NAME_HISTOGRAM = "histogram";
  @SerializedName(SERIALIZED_NAME_HISTOGRAM)
  private V1EventHistogram histogram;

  public static final String SERIALIZED_NAME_AUDIO = "audio";
  @SerializedName(SERIALIZED_NAME_AUDIO)
  private V1EventAudio audio;

  public static final String SERIALIZED_NAME_VIDEO = "video";
  @SerializedName(SERIALIZED_NAME_VIDEO)
  private V1EventVideo video;

  public static final String SERIALIZED_NAME_HTML = "html";
  @SerializedName(SERIALIZED_NAME_HTML)
  private String html;

  public static final String SERIALIZED_NAME_TEXT = "text";
  @SerializedName(SERIALIZED_NAME_TEXT)
  private String text;

  public static final String SERIALIZED_NAME_CHART = "chart";
  @SerializedName(SERIALIZED_NAME_CHART)
  private V1EventChart chart;

  public static final String SERIALIZED_NAME_MODEL = "model";
  @SerializedName(SERIALIZED_NAME_MODEL)
  private V1EventModel model;

  public static final String SERIALIZED_NAME_ARTIFACT = "artifact";
  @SerializedName(SERIALIZED_NAME_ARTIFACT)
  private V1EventArtifact artifact;

  public static final String SERIALIZED_NAME_DATAFRAME = "dataframe";
  @SerializedName(SERIALIZED_NAME_DATAFRAME)
  private V1EventDataframe dataframe;

  public static final String SERIALIZED_NAME_CURVE = "curve";
  @SerializedName(SERIALIZED_NAME_CURVE)
  private V1EventCurve curve;


  public V1Event timestamp(OffsetDateTime timestamp) {
    
    this.timestamp = timestamp;
    return this;
  }

   /**
   * Get timestamp
   * @return timestamp
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public OffsetDateTime getTimestamp() {
    return timestamp;
  }


  public void setTimestamp(OffsetDateTime timestamp) {
    this.timestamp = timestamp;
  }


  public V1Event step(Integer step) {
    
    this.step = step;
    return this;
  }

   /**
   * Global step of the event.
   * @return step
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "Global step of the event.")

  public Integer getStep() {
    return step;
  }


  public void setStep(Integer step) {
    this.step = step;
  }


  public V1Event metric(Float metric) {
    
    this.metric = metric;
    return this;
  }

   /**
   * Get metric
   * @return metric
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Float getMetric() {
    return metric;
  }


  public void setMetric(Float metric) {
    this.metric = metric;
  }


  public V1Event image(V1EventImage image) {
    
    this.image = image;
    return this;
  }

   /**
   * Get image
   * @return image
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1EventImage getImage() {
    return image;
  }


  public void setImage(V1EventImage image) {
    this.image = image;
  }


  public V1Event histogram(V1EventHistogram histogram) {
    
    this.histogram = histogram;
    return this;
  }

   /**
   * Get histogram
   * @return histogram
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1EventHistogram getHistogram() {
    return histogram;
  }


  public void setHistogram(V1EventHistogram histogram) {
    this.histogram = histogram;
  }


  public V1Event audio(V1EventAudio audio) {
    
    this.audio = audio;
    return this;
  }

   /**
   * Get audio
   * @return audio
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1EventAudio getAudio() {
    return audio;
  }


  public void setAudio(V1EventAudio audio) {
    this.audio = audio;
  }


  public V1Event video(V1EventVideo video) {
    
    this.video = video;
    return this;
  }

   /**
   * Get video
   * @return video
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1EventVideo getVideo() {
    return video;
  }


  public void setVideo(V1EventVideo video) {
    this.video = video;
  }


  public V1Event html(String html) {
    
    this.html = html;
    return this;
  }

   /**
   * Get html
   * @return html
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getHtml() {
    return html;
  }


  public void setHtml(String html) {
    this.html = html;
  }


  public V1Event text(String text) {
    
    this.text = text;
    return this;
  }

   /**
   * Get text
   * @return text
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getText() {
    return text;
  }


  public void setText(String text) {
    this.text = text;
  }


  public V1Event chart(V1EventChart chart) {
    
    this.chart = chart;
    return this;
  }

   /**
   * Get chart
   * @return chart
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1EventChart getChart() {
    return chart;
  }


  public void setChart(V1EventChart chart) {
    this.chart = chart;
  }


  public V1Event model(V1EventModel model) {
    
    this.model = model;
    return this;
  }

   /**
   * Get model
   * @return model
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1EventModel getModel() {
    return model;
  }


  public void setModel(V1EventModel model) {
    this.model = model;
  }


  public V1Event artifact(V1EventArtifact artifact) {
    
    this.artifact = artifact;
    return this;
  }

   /**
   * Get artifact
   * @return artifact
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1EventArtifact getArtifact() {
    return artifact;
  }


  public void setArtifact(V1EventArtifact artifact) {
    this.artifact = artifact;
  }


  public V1Event dataframe(V1EventDataframe dataframe) {
    
    this.dataframe = dataframe;
    return this;
  }

   /**
   * Get dataframe
   * @return dataframe
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1EventDataframe getDataframe() {
    return dataframe;
  }


  public void setDataframe(V1EventDataframe dataframe) {
    this.dataframe = dataframe;
  }


  public V1Event curve(V1EventCurve curve) {
    
    this.curve = curve;
    return this;
  }

   /**
   * Get curve
   * @return curve
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1EventCurve getCurve() {
    return curve;
  }


  public void setCurve(V1EventCurve curve) {
    this.curve = curve;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    V1Event v1Event = (V1Event) o;
    return Objects.equals(this.timestamp, v1Event.timestamp) &&
        Objects.equals(this.step, v1Event.step) &&
        Objects.equals(this.metric, v1Event.metric) &&
        Objects.equals(this.image, v1Event.image) &&
        Objects.equals(this.histogram, v1Event.histogram) &&
        Objects.equals(this.audio, v1Event.audio) &&
        Objects.equals(this.video, v1Event.video) &&
        Objects.equals(this.html, v1Event.html) &&
        Objects.equals(this.text, v1Event.text) &&
        Objects.equals(this.chart, v1Event.chart) &&
        Objects.equals(this.model, v1Event.model) &&
        Objects.equals(this.artifact, v1Event.artifact) &&
        Objects.equals(this.dataframe, v1Event.dataframe) &&
        Objects.equals(this.curve, v1Event.curve);
  }

  @Override
  public int hashCode() {
    return Objects.hash(timestamp, step, metric, image, histogram, audio, video, html, text, chart, model, artifact, dataframe, curve);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class V1Event {\n");
    sb.append("    timestamp: ").append(toIndentedString(timestamp)).append("\n");
    sb.append("    step: ").append(toIndentedString(step)).append("\n");
    sb.append("    metric: ").append(toIndentedString(metric)).append("\n");
    sb.append("    image: ").append(toIndentedString(image)).append("\n");
    sb.append("    histogram: ").append(toIndentedString(histogram)).append("\n");
    sb.append("    audio: ").append(toIndentedString(audio)).append("\n");
    sb.append("    video: ").append(toIndentedString(video)).append("\n");
    sb.append("    html: ").append(toIndentedString(html)).append("\n");
    sb.append("    text: ").append(toIndentedString(text)).append("\n");
    sb.append("    chart: ").append(toIndentedString(chart)).append("\n");
    sb.append("    model: ").append(toIndentedString(model)).append("\n");
    sb.append("    artifact: ").append(toIndentedString(artifact)).append("\n");
    sb.append("    dataframe: ").append(toIndentedString(dataframe)).append("\n");
    sb.append("    curve: ").append(toIndentedString(curve)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

