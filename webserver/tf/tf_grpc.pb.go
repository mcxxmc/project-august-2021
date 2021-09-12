// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package tf

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// CommunicatorClient is the client API for Communicator service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type CommunicatorClient interface {
	// ask for new images to predict
	RequestImages(ctx context.Context, in *TFStandard, opts ...grpc.CallOption) (*ImageArray, error)
	// exchange the prediction results
	PostPredictions(ctx context.Context, in *PredictionArray, opts ...grpc.CallOption) (*TFStandard, error)
}

type communicatorClient struct {
	cc grpc.ClientConnInterface
}

func NewCommunicatorClient(cc grpc.ClientConnInterface) CommunicatorClient {
	return &communicatorClient{cc}
}

func (c *communicatorClient) RequestImages(ctx context.Context, in *TFStandard, opts ...grpc.CallOption) (*ImageArray, error) {
	out := new(ImageArray)
	err := c.cc.Invoke(ctx, "/Communicator/RequestImages", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *communicatorClient) PostPredictions(ctx context.Context, in *PredictionArray, opts ...grpc.CallOption) (*TFStandard, error) {
	out := new(TFStandard)
	err := c.cc.Invoke(ctx, "/Communicator/PostPredictions", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// CommunicatorServer is the server API for Communicator service.
// All implementations must embed UnimplementedCommunicatorServer
// for forward compatibility
type CommunicatorServer interface {
	// ask for new images to predict
	RequestImages(context.Context, *TFStandard) (*ImageArray, error)
	// exchange the prediction results
	PostPredictions(context.Context, *PredictionArray) (*TFStandard, error)
	mustEmbedUnimplementedCommunicatorServer()
}

// UnimplementedCommunicatorServer must be embedded to have forward compatible implementations.
type UnimplementedCommunicatorServer struct {
}

func (UnimplementedCommunicatorServer) RequestImages(context.Context, *TFStandard) (*ImageArray, error) {
	return nil, status.Errorf(codes.Unimplemented, "method RequestImages not implemented")
}
func (UnimplementedCommunicatorServer) PostPredictions(context.Context, *PredictionArray) (*TFStandard, error) {
	return nil, status.Errorf(codes.Unimplemented, "method PostPredictions not implemented")
}
func (UnimplementedCommunicatorServer) mustEmbedUnimplementedCommunicatorServer() {}

// UnsafeCommunicatorServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to CommunicatorServer will
// result in compilation errors.
type UnsafeCommunicatorServer interface {
	mustEmbedUnimplementedCommunicatorServer()
}

func RegisterCommunicatorServer(s grpc.ServiceRegistrar, srv CommunicatorServer) {
	s.RegisterService(&Communicator_ServiceDesc, srv)
}

func _Communicator_RequestImages_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(TFStandard)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(CommunicatorServer).RequestImages(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Communicator/RequestImages",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(CommunicatorServer).RequestImages(ctx, req.(*TFStandard))
	}
	return interceptor(ctx, in, info, handler)
}

func _Communicator_PostPredictions_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PredictionArray)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(CommunicatorServer).PostPredictions(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Communicator/PostPredictions",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(CommunicatorServer).PostPredictions(ctx, req.(*PredictionArray))
	}
	return interceptor(ctx, in, info, handler)
}

// Communicator_ServiceDesc is the grpc.ServiceDesc for Communicator service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Communicator_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "Communicator",
	HandlerType: (*CommunicatorServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "RequestImages",
			Handler:    _Communicator_RequestImages_Handler,
		},
		{
			MethodName: "PostPredictions",
			Handler:    _Communicator_PostPredictions_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "tf.proto",
}