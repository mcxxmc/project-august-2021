// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        v3.14.0
// source: tf_fast.proto

package tf_fast

import (
	tf "webserver/tf"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

var File_tf_fast_proto protoreflect.FileDescriptor

var file_tf_fast_proto_rawDesc = []byte{
	0x0a, 0x0d, 0x74, 0x66, 0x5f, 0x66, 0x61, 0x73, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a,
	0x08, 0x74, 0x66, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x32, 0x3c, 0x0a, 0x12, 0x49, 0x6d, 0x6d,
	0x65, 0x64, 0x69, 0x61, 0x74, 0x65, 0x50, 0x72, 0x65, 0x64, 0x69, 0x63, 0x74, 0x6f, 0x72, 0x12,
	0x26, 0x0a, 0x0d, 0x49, 0x6d, 0x6d, 0x65, 0x64, 0x69, 0x61, 0x74, 0x65, 0x50, 0x72, 0x65, 0x64,
	0x12, 0x06, 0x2e, 0x49, 0x6d, 0x61, 0x67, 0x65, 0x1a, 0x0b, 0x2e, 0x50, 0x72, 0x65, 0x64, 0x69,
	0x63, 0x74, 0x69, 0x6f, 0x6e, 0x22, 0x00, 0x42, 0x0b, 0x5a, 0x09, 0x2e, 0x2f, 0x74, 0x66, 0x5f,
	0x66, 0x61, 0x73, 0x74, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var file_tf_fast_proto_goTypes = []interface{}{
	(*tf.Image)(nil),      // 0: Image
	(*tf.Prediction)(nil), // 1: Prediction
}
var file_tf_fast_proto_depIdxs = []int32{
	0, // 0: ImmediatePredictor.ImmediatePred:input_type -> Image
	1, // 1: ImmediatePredictor.ImmediatePred:output_type -> Prediction
	1, // [1:2] is the sub-list for method output_type
	0, // [0:1] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_tf_fast_proto_init() }
func file_tf_fast_proto_init() {
	if File_tf_fast_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_tf_fast_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   0,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_tf_fast_proto_goTypes,
		DependencyIndexes: file_tf_fast_proto_depIdxs,
	}.Build()
	File_tf_fast_proto = out.File
	file_tf_fast_proto_rawDesc = nil
	file_tf_fast_proto_goTypes = nil
	file_tf_fast_proto_depIdxs = nil
}