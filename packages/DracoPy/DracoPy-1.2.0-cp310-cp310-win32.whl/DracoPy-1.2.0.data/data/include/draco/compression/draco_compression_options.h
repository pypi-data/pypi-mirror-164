// Copyright 2019 The Draco Authors.
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
//
#ifndef DRACO_COMPRESSION_DRACO_COMPRESSION_OPTIONS_H_
#define DRACO_COMPRESSION_DRACO_COMPRESSION_OPTIONS_H_

#include "draco/draco_features.h"

#ifdef DRACO_TRANSCODER_SUPPORTED
#include "draco/core/status.h"

namespace draco {
// TODO(fgalligan): Add support for unified_position_quantization.
// Struct to hold Draco compression options.
struct DracoCompressionOptions {
  int compression_level = 7;  // compression level [0-10], most=10, least=0.
  int quantization_bits_position = 11;
  int quantization_bits_normal = 8;
  int quantization_bits_tex_coord = 10;
  int quantization_bits_color = 8;
  int quantization_bits_generic = 8;
  int quantization_bits_tangent = 8;
  int quantization_bits_weight = 8;
  bool find_non_degenerate_texture_quantization = false;

  bool operator==(const DracoCompressionOptions &other) const {
    return compression_level == other.compression_level &&
           quantization_bits_position == other.quantization_bits_position &&
           quantization_bits_normal == other.quantization_bits_normal &&
           quantization_bits_tex_coord == other.quantization_bits_tex_coord &&
           quantization_bits_color == other.quantization_bits_color &&
           quantization_bits_generic == other.quantization_bits_generic &&
           quantization_bits_tangent == other.quantization_bits_tangent &&
           quantization_bits_weight == other.quantization_bits_weight &&
           find_non_degenerate_texture_quantization ==
               other.find_non_degenerate_texture_quantization;
  }

  bool operator!=(const DracoCompressionOptions &other) const {
    return !(*this == other);
  }

  Status Check() const {
    DRACO_RETURN_IF_ERROR(
        Validate("Compression level", compression_level, 0, 10));
    DRACO_RETURN_IF_ERROR(
        Validate("Position quantization", quantization_bits_position, 0, 30));
    DRACO_RETURN_IF_ERROR(
        Validate("Normals quantization", quantization_bits_normal, 0, 30));
    DRACO_RETURN_IF_ERROR(
        Validate("Tex coord quantization", quantization_bits_tex_coord, 0, 30));
    DRACO_RETURN_IF_ERROR(
        Validate("Color quantization", quantization_bits_color, 0, 30));
    DRACO_RETURN_IF_ERROR(
        Validate("Generic quantization", quantization_bits_generic, 0, 30));
    DRACO_RETURN_IF_ERROR(
        Validate("Tangent quantization", quantization_bits_tangent, 0, 30));
    DRACO_RETURN_IF_ERROR(
        Validate("Weights quantization", quantization_bits_weight, 0, 30));
    return OkStatus();
  }

  static Status Validate(const std::string &name, int value, int min, int max) {
    if (value < min || value > max) {
      const std::string range =
          "[" + std::to_string(min) + "-" + std::to_string(max) + "].";
      return Status(Status::DRACO_ERROR, name + " is out of range " + range);
    }
    return OkStatus();
  }
};

}  // namespace draco

#endif  // DRACO_TRANSCODER_SUPPORTED
#endif  // DRACO_COMPRESSION_DRACO_COMPRESSION_OPTIONS_H_
